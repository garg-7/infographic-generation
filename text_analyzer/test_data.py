from flask_cors import CORS
from torch.utils.data import DataLoader
from create_encodings import get_encodings_from_raw_text
import torch
import numpy as np
from flask import Flask, request

app = Flask(__name__)
CORS(app)

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


@app.route('/tokenize', methods=['POST', ])
def tokenize():
    print("hello")
    json = request.get_json()
    text = json['text']
    test_encodings, _ = get_encodings_from_raw_text(text)
    test_dataset = VariationDataset(test_encodings, _)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    print(f'Device to be used: {device}')

    model = torch.load('merged_model.pt')
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
    time = ""
    parameter = ""
    country = ""
    value = ""
    for idx, val in enumerate(tokens):
        if tags[idx] in ["B-T", 'I-T']:
            time = time + val + " "
        elif tags[idx] in ["B-P", 'I-P']:
            parameter = parameter + val + " "
        elif tags[idx] in ["B-C", 'I-C']:
            country = country + val + " "
        elif tags[idx] in ["B-V", 'I-V']:
            if val.isnumeric() or val == "." or val == "%":
                value = value + val + " "

    return {
        "time": time.rstrip(),
        "parameter": parameter.rstrip(),
        "country": country.rstrip(),
        "value": "".join(value.split())
    }


if __name__ == '__main__':
    app.run(debug=True)
