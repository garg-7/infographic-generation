# infographic-generation

Infographic Generation System made for 5th semester B.Tech Project under the guidance of Prof. Chiranjoy Chattopadhyay

## Getting Started

* Navigate to the cloned repository.
```
cd infographic-generation
```
### Backend Setup

* Set up and activate a virtual environment
```
sudo apt-get install -y python3-venv
python3 -m venv env
source env/bin/activate
```
* Use pip to install other dependencies from `req.txt` 
```
pip install -r req.txt
```

* Run the server 
```
python test_data.py
```
### Frontend Setup

Note: `npm` must be installed in the computer

* In a new terminal window navigate to `graphics_generator` folder
```
cd graphics_generator
```

* Install dependencies from `package.json`
```
npm install
```

* Run development server 
```
npm start
```

The frontend of the application must now be running at `localhost:3000`
