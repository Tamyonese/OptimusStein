import json
import os
from datetime import datetime, timedelta
from config import DATA_FILE

def load_data():
    # Lädt die Benutzerdaten aus der JSON-Datei.
    if not os.path.isfile(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Fehler beim Laden der Daten: {e}")
        return {}

def save_data(data):
    # Speichert die Benutzerdaten in der JSON-Datei.
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Fehler beim Speichern der Daten: {e}")

def has_claimed_daily(user_data):
    last_claim = datetime.strptime(user_data.get('last_claim', '2000-01-01'), '%Y-%m-%d')
    return datetime.now() <= last_claim + timedelta(days=1)
