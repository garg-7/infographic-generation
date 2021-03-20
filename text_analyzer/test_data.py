from torch.utils.data import DataLoader
from create_encodings import get_encodings_from_raw_text
import torch
import numpy as np


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


unique_tags = [
    'O',  # participates in no entity
    'B-T',  # beginning of time period
    'I-T',  # in time period
    'B-P',  # beginning of parameter
    'I-P',  # in parameter
    'B-C',  # beginning of country
    'I-C',  # in country
    'B-V',  # beginning of value
    'I-V',  # in value
]

tag2id = {tag: id for id, tag in enumerate(unique_tags)}
id2tag = {id: tag for tag, id in tag2id.items()}

test_encodings, _ = get_encodings_from_raw_text('raw_text.txt')
test_dataset = VariationDataset(test_encodings, _)
test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print(f'Device to be used: {device}')

model = torch.load('merged_model.pt')
model.to(device)
model.eval()
results_file = open('raw_text_result.txt', 'w')
for batch in test_loader:
    input_ids = batch['input_ids'].to(device)
    attention_mask = batch['attention_mask'].to(device)
    outputs = model(input_ids, attention_mask == attention_mask)
    output_tags = np.argmax(outputs[0].detach().cpu().numpy(), axis=2)[0]
    for i in output_tags:
        print(id2tag[i], end=' ')
        results_file.write(id2tag[i] + ' ')
    results_file.write('\n')
    print()
