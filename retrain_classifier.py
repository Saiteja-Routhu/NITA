import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data_path = r"C:\Users\saite\NITA\NITA\data\commands.csv"
vectorizer_path = r"C:\Users\saite\NITA\NITA\models\vectorizer.pkl"
model_path = r"C:\Users\saite\NITA\NITA\models\command_classifier.pkl"

# ✅ Load and preprocess data
def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    X = data['command']
    y = data['action']
    return X, y

X, y = load_and_preprocess_data(data_path)

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vectorized, y)

with open(vectorizer_path, "wb") as f:
    pickle.dump(vectorizer, f)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model retrained and saved successfully.")
