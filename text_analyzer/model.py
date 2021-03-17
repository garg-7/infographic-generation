import sys
from torch.utils import data
from transformers import DistilBertForTokenClassification
from transformers import DistilBertTokenizerFast
from transformers import  AdamW
import numpy as np
import torch
import random
from torch.utils.data import DataLoader, dataset
from create_encodings import main as encodings_from_text
from create_encodings import get_encodings_from_raw_text
from datetime import datetime

class VariationDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# for i in range(len(encodings['attention_mask'])):
#     assert len(encodings['input_ids'][i])==len(final_tag_ids[i])
#     for k in encodings['input_ids'][i]:
#         print(tokenizer.decode(k), end=' ')
#     print()
#     for k in final_tag_ids[i]:
#         print(k, end=' ')
#     print()
#     print(encodings['attention_mask'][i])
# sys.exit()

unique_tags = [
        'O',        # participates in no entity
        'B-T',      # beginning of time period
        'I-T',      # in time period
        'B-P',      # beginning of parameter
        'I-P',      # in parameter
        'B-C',      # beginning of country
        'I-C',      # in country
        'B-V',      # beginning of value
        'I-V',      # in value
    ]

tag2id = {tag: id for id, tag in enumerate(unique_tags)}
id2tag = {id: tag for tag, id in tag2id.items()}

train_encodings, train_labels = encodings_from_text('train.txt')
val_encodings, val_labels = encodings_from_text('val.txt')

test_encodings, _ = get_encodings_from_raw_text('raw_text.txt')

train_dataset = VariationDataset(train_encodings, train_labels)
print(f'Train dataset length: {len(train_dataset)}')
val_dataset = VariationDataset(val_encodings, val_labels)
print(f'Val dataset length: {len(val_dataset)}')
test_dataset = VariationDataset(test_encodings, _)
print(f'Test dataset length: {len(test_dataset)}')

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(f'Device to be used: {device}')

BATCH_SIZE = 32

train_loader = DataLoader(train_dataset, batch_size = BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size = 1, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size = 1, shuffle=False)
# for i in train_loader:
#     for j in i['input_ids']:
#         print(tokenizer.decode(j), end=' ')
#     print()
#     for k in i['labels']:
#         print(k, end=' ')
#     print()
#     break
# sys.exit()


####### TRAINING CODE #########
print('-------TRAINING-------')
model = DistilBertForTokenClassification.from_pretrained('distilbert-base-cased', num_labels=len(unique_tags))

model.to(device)
model.train()
optim = AdamW(model.parameters(), lr=5e-5)

num_epochs = 2

resp = input('Skip training?')
if resp.lower()=='n':
    for epoch in range(num_epochs):
        for b, batch in enumerate(train_loader):
            # print(len(batch['input_ids']))
            optim.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs[0]
            print(f'[Epoch: {epoch+1}/{num_epochs}][Batch: {b+1}/{len(train_dataset)/BATCH_SIZE:.0f}] Loss: {loss}')
            loss.backward()
            optim.step()

    print('Saving trained model...')
    # torch.save(model, f'merged_model{datetime.now().strftime("%d/%m/%Y_%H.%M.%S")}.pt')
    torch.save(model, 'merged_model.pt')
    # sys.exit()
###############################



####### VALIDATION CODE ########

print('-------VALIDATION-------')
model = torch.load('merged_model.pt')
model.to(device)
model.eval()
count=0
corrects = 0
print('Sentence Accs:')
for batch in val_loader:
    sentence_acc = 0
    sentence_corrects = 0
    sentence_wrongs = 0
    input_ids = batch['input_ids'].to(device)
    # for i in input_ids:
        # print(tokenizer.decode(i),end=' ')
    # print('\n-------------')
    attention_mask = batch['attention_mask'].to(device)
    labels = batch['labels'].to(device)
    outputs = model(input_ids, attention_mask==attention_mask)
    # print(outputs[0])
    # print(batch['labels'].cpu().numpy())
    output_tags = np.argmax(outputs[0].detach().cpu().numpy(), axis=2)[0]
    for i, tag_gt in enumerate(batch['labels'].detach().cpu().numpy()[0]):
        if tag_gt!=-100:
            count+=1
            if tag_gt==output_tags[i]:
                sentence_corrects+=1
                corrects+=1
            else:
                sentence_wrongs+=1
    sentence_acc = sentence_corrects/(sentence_corrects+sentence_wrongs)*100
    # print(f'{sentence_acc:.2f}', end=' ')
    # print(np.argmax(outputs[1].detach().cpu().numpy(), axis=2))
    # print('-------------')

print(f'Overall number of tokens: {count}')
print(f'Overall acc: {corrects/count*100:.2f}')
#############################

####### TESTING CODE ########
print('-------TESTING-------')

# model = torch.load('merged_model.pt')
# model.to(device)
# model.eval()

results_file = open('raw_text_result.txt', 'w')
for batch in test_loader:
    input_ids = batch['input_ids'].to(device)
    attention_mask = batch['attention_mask'].to(device)
    outputs = model(input_ids, attention_mask==attention_mask)
    output_tags = np.argmax(outputs[0].detach().cpu().numpy(), axis=2)[0]
    for i in output_tags:
        print(id2tag[i], end=' ')
        results_file.write(id2tag[i]+' ')
    results_file.write('\n')
    print()
#############################