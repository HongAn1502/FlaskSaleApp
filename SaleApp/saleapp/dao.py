import json
from saleapp.templates._init_ import app

def load_categories():
    with open(f'{app.root_path}/data/categories.json', encoding='utf-8') as f:
        return json.load