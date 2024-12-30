import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import string
from langdetect import detect

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


def stem_text(text):
    stemmer = SnowballStemmer('spanish')
    tokens = text.split()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = text.split()
    lemmatized_tokens = [lemmatizer.lemmatize(token, pos='v') for token in tokens]  # 'v' for verbs
    return ' '.join(lemmatized_tokens)

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def normalize_text(text):
    text = text.lower()
    text = ''.join([char for char in text if not char.isdigit()])
    return text

def detect_language(text):
    return detect(text)