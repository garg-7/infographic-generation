# Infographics from Sports headlines

## Requirements

To train & test the model declared in `model.py`, the following are needed:

`torch==1.8.1`  
`transformers==4.5.1`  
`numpy==1.19.4`  


Note: The following are not required now. Just for future use, the raw data about the teams and tournaments was scraped using:

`beautifulsoup4==4.9.3`  
`lxml==4.6.3`  

## Generating sentences

To create sentences, simply run the following:
```
python3 generator.py
```

To split them into train and validation sets after shuffling:
```
python3 train_val_splitter.py
```

NOTE: Do not rename anything. Just run the above commands sequentially and the required training and testing files will be created.
## Training and testing

The following would first train the model then test it, using the sentences created above.
```
python3 model.py
```

