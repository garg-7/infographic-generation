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


def test_sports(text):
    print(text)

    test_encodings, _ = get_encodings_from_raw_text(text)
    test_dataset = VariationDataset(test_encodings, _)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    print(f'Device to be used: {device}')

    model = torch.load('sports_model.pt')
    model.to(device)
    model.eval()
    results_file = open('raw_text_result.txt', 'w')
    tags = []
    for batch in test_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        outputs = model(input_ids, attention_mask == attention_mask)
        output_tags = np.argmax(outputs[0].detach().cpu().numpy(), axis=2)[0]
        for i in output_tags:
            print(id2tag[i], end=' ')
            tags.append(id2tag[i])
            results_file.write(id2tag[i] + ' ')
        results_file.write('\n')
        print()
    tags.pop(0)
    tags.pop()
    tokens = text.split()
    sport = ""
    winning_team = ""
    losing_team = ""
    score = ""
    match = ""
    for idx, val in enumerate(tokens):
        if tags[idx] in ["B-S", 'I-S']:
            sport = sport + val + " "
        elif tags[idx] in ["B-WT", 'I-WT']:
            winning_team = winning_team + val + " "
        elif tags[idx] in ["B-LT", 'I-LT']:
            losing_team = losing_team + val + " "
        elif tags[idx] in ["B-G", 'I-G']:
            score = score + val + " "
        elif tags[idx] in ["B-M", 'I-M']:
            match = match + val + " "

    t = {
        "sport": sport.rstrip(),
        "winning_team": winning_team.rstrip(),
        "losing_team": losing_team.rstrip(),
        "score": score.rstrip(),
        "match": match.rstrip(),
    }
    print(t)
    return t


test_sports("Cricket : World no. 1 New Zealand pip Bangladesh by 74 runs to win ICC Mens Cricket World Cup .")
