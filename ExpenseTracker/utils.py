import json
import os
from datetime import datetime

DATA_FILE = "user_data.json"

def load_user_data(username):
    
    if not os.path.exists(DATA_FILE):
        return None
        
    with open(DATA_FILE, 'r') as f:
        all_data = json.load(f)
        return all_data.get(username)

def save_user_data(username, data):
    
    all_data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            all_data = json.load(f)
    
    all_data[username] = data
    with open(DATA_FILE, 'w') as f:
        json.dump(all_data, f, indent=2)

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")