# flask-restful-crud

## Setup the project

Init a virtual environment.

```bash
python3 -m venv env
source env/bin/activate 
```

Install the dependencies.

```bash
pip install -r requirements.txt 
```

## Running the project

Start the API

```bash
python3 api.py 
```

Open your Postman application and import the `postman_collection.json` collection and start making request to the API.

## Tasks dict example

```python
TASKS = {
  "12345": {
    "id": "12345",
    "task": "Play Guitar"
  },
  "12346": {
    "id": "12346",
    "task": "Play Drums"
  }
}
```
