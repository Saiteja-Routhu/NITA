import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    """Cleans and processes text data."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]', '', text)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

def tokenize_and_stem(text):
    """Tokenizes and stems text."""
    words = clean_text(text).split()
    stemmer = nltk.PorterStemmer()
    return [stemmer.stem(word) for word in words]
