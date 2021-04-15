from torch.utils import data
from transformers import DistilBertForTokenClassification
from transformers import DistilBertTokenizerFast
from transformers import AdamW
import numpy as np
import torch
import random
from torch.utils.data import DataLoader, dataset
from create_encodings import main as encodings_from_text
from create_encodings import get_encodings_from_raw_text


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
    'B-S',  # sport
    'I-S',  #
    'B-WT',  # winning team
    'I-WT',  #
    'B-LT',  # losing team
    'I-LT',  #
    'B-G',  # score gap
    'I-G',  #
    'B-M',  # match/tournament title
    'I-M',  #
]

tag2id = {tag: id for id, tag in enumerate(unique_tags)}
id2tag = {id: tag for tag, id in tag2id.items()}


def test_sports():
    text = "Cricket : World no. 1 South Africa beat England by 35 runs ."

    test_encodings, _ = get_encodings_from_raw_text('raw_text.txt')
    test_dataset = VariationDataset(test_encodings, _)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    print(f'Device to be used: {device}')

    model = torch.load('sports_model.pt')
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

test_sports()
