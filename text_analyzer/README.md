# The Text Analyzer Module

## Requirements

Install the requirements as mentioned from the `req.txt` file.

## Working

Run `model.py` to train, validate and test the model on the dataset. 

```bash 
python model.py
```
It picks up data from the following files:
- Training data from `train.txt` (ground truth from `train_gt.txt`) [Probably don't want to change this.]
- Validation data from `val.txt` (ground truth from `val_gt.txt`) [Probably don't want to change this either.]
- Testing data from `raw_text.txt` [Change this]

## Testing on raw text

To test the model on raw text once it is trained, put raw sentences in the `raw_text.txt` file.
Format of the sentences must be kept in mind. Every token should be space separated, like the sample sentence given.
E.g. for 23.54% you need to write 23 . 54 % (this would save an intermediate tokenization step ;-) ).
