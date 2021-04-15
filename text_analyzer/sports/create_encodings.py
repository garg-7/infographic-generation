import sys
from transformers import DistilBertForTokenClassification
from transformers import DistilBertTokenizerFast
from transformers import  AdamW
import numpy as np
import torch
import random
from torch.utils.data import DataLoader

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

def main(text_file):
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-cased')

    unique_tags = [
        'O',        # participates in no entity
        'B-S',      # sport
        'I-S',      # 
        'B-WT',      # winning team
        'I-WT',      # 
        'B-LT',      # losing team
        'I-LT',      # 
        'B-G',      # score gap
        'I-G',      # 
        'B-M',      # match/tournament title
        'I-M',      # 
    ]

    tag2id = {tag: id for id, tag in enumerate(unique_tags)}
    id2tag = {id: tag for tag, id in tag2id.items()}

    texts = []
    tags = []

    f = list(open(text_file, 'r').readlines())
    f_gt = list(open(text_file.replace('.txt', '_gt.txt'), 'r').readlines())
    assert len(f)==len(f_gt)

    for i, line in enumerate(f):
        tokens = line.strip().split(' ')
        labels = f_gt[i].strip().split(' ')
        try:
            assert len(tokens)==len(labels)
        except AssertionError:
            print(tokens)
            print(labels)
            exit()
        texts.append(tokens)
        tags.append(labels)

    tag_idxes = []
    new_tokens = []

    for i in range(len(texts)):# for every sentence
        new_label_indices = []
        tokens_for_current_sentence = []
        for j, text in enumerate(texts[i]): # for every word
            tokens = tokenizer.tokenize(text) # tokenize the word
            tokens_for_current_sentence.extend(tokens)
            if len(tokens)==1:  # if only one token for the word
                new_label_indices.append(tag2id[tags[i][j]])    # add the label index directly
            else:   # if the word is split i.e. multiple subtokens
                if tags[i][j].startswith('B-'): # if the split one's label begins with B-
                    intermediate = tags[i][j].replace('B', 'I')
                    new_label_indices.append(tag2id[tags[i][j]])    # put on B- and rest (I-)'s
                    for _ in range(len(tokens)-1):
                        new_label_indices.append(tag2id[intermediate])  
                else:               # if the split one's label begins with I- or O just repeat them
                    for _ in range(len(tokens)):
                        new_label_indices.append(tag2id[tags[i][j]])
        
        assert len(tokens_for_current_sentence)==len(new_label_indices)
        
        # add ending and beginning tokens
        tokens_for_current_sentence.insert(0, '[CLS]')
        new_label_indices.insert(0, 0)
        last_idx = len(tokens_for_current_sentence)
        tokens_for_current_sentence.insert(last_idx, '[SEP]')
        new_label_indices.insert(last_idx, 0)
        
        new_tokens.append(tokens_for_current_sentence)
        tag_idxes.append(new_label_indices)

    # check for the longest sentence 
    max_len = len(new_tokens[0])
    for i in new_tokens:
        if len(i)>max_len:
            max_len = len(i)

    # pad and create the final IDs
    token_ids = [] 
    final_tag_ids = []
    attention_masks = []
    for i in range(len(new_tokens)): # for every sentence
        curr_sentence_tokens = new_tokens[i]    # tokens of a sentence
        curr_sentence_tags = tag_idxes[i]       # indices of labels of tokens for the sentence
        curr_attention_mask = [1]*len(curr_sentence_tags) 
        if len(curr_sentence_tokens)<max_len:
            diff = max_len - len(curr_sentence_tokens)
            for _ in range(diff):
                curr_sentence_tokens.append('[PAD]')
                curr_sentence_tags.append(-100)
                curr_attention_mask.append(0)   # 0 attention_mask value for [PAD] tokens
        curr_token_ids = [] # to store the ids of tokens in the current sentence from the vocab
        for token in curr_sentence_tokens:
            curr_token_ids.append(tokenizer.convert_tokens_to_ids(token))
        assert len(curr_token_ids)==len(curr_sentence_tags)
        token_ids.append(curr_token_ids)
        final_tag_ids.append(curr_sentence_tags)
        attention_masks.append(curr_attention_mask)

    encodings = {}

    encodings['input_ids'] = token_ids
    encodings['attention_mask'] = attention_masks
    return encodings, final_tag_ids

def get_encodings_from_raw_text(sentence):
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-cased')
    texts = []

    # f = list(open(text_file, 'r').readlines())
    f = list()
    f.append(sentence)

    for i, line in enumerate(f):
        tokens = line.strip().split(' ')
        texts.append(tokens)

    new_tokens = []

    for i in range(len(texts)):# for every sentence
        tokens_for_current_sentence = []
        for j, text in enumerate(texts[i]): # for every word
            tokens = tokenizer.tokenize(text) # tokenize the word
            tokens_for_current_sentence.extend(tokens)
         
        # add ending and beginning tokens
        tokens_for_current_sentence.insert(0, '[CLS]')
        last_idx = len(tokens_for_current_sentence)
        tokens_for_current_sentence.insert(last_idx, '[SEP]')
                
        new_tokens.append(tokens_for_current_sentence)

    # check for the longest sentence 
    max_len = len(new_tokens[0])
    for i in new_tokens:
        if len(i)>max_len:
            max_len = len(i)

    # create the final IDs
    token_ids = [] 
    attention_masks = []
    labels = []
    for i in range(len(new_tokens)): # for every sentence
        curr_sentence_tokens = new_tokens[i]    # tokens of a sentence
        curr_attention_mask = [1]*len(curr_sentence_tokens) 
        curr_labels = [0]*len(curr_attention_mask)
        curr_token_ids = [] # to store the ids of tokens in the current sentence from the vocab
        for token in curr_sentence_tokens:
            curr_token_ids.append(tokenizer.convert_tokens_to_ids(token))
        token_ids.append(curr_token_ids)
        attention_masks.append(curr_attention_mask)
        labels.append(curr_labels)
    encodings = {}

    encodings['input_ids'] = token_ids
    encodings['attention_mask'] = attention_masks

    return encodings, labels

if __name__ == '__main__':
    main('data.txt')