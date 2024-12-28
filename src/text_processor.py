import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('spanish'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return " ".join(filtered_text)

def process_text(text):
    # Text normalization
    text = text.lower()
    # Removing stopwords
    text = remove_stopwords(text)
    return text
