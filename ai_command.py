import pickle
import os
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

vectorizer_path = r"C:\Users\saite\NITA\NITA\models\vectorizer.pkl"
model_path = r"C:\Users\saite\NITA\NITA\models\command_classifier.pkl"

with open(vectorizer_path, "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def clean_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

def predict_action(command):
    try:
        cleaned = clean_text(command)
        command_vector = vectorizer.transform([cleaned])
        prediction = model.predict(command_vector)[0]
        return prediction
    except Exception as e:
        print(f"Error predicting action: {e}")
        return "ai:conversation"

if __name__ == "__main__":
    print("🔍 Testing command prediction...")
    while True:
        user_input = input("\nType a command (or 'exit' to stop): ")
        if user_input.lower() == "exit":
            break

        action = predict_action(user_input)
        print(f"Predicted Action: {action}")
