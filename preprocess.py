import pandas as pd
from modules.nlp import clean_text

def load_and_preprocess_data(csv_path):
    """Loads and preprocesses command data from CSV."""
    try:
        data = pd.read_csv(csv_path)
        data['cleaned_command'] = data['command'].apply(clean_text)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
