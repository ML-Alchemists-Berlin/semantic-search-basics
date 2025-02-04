import pandas as pd
import re
import spacy

# Load German language model from spaCy
nlp = spacy.load("de_core_news_sm")

def clean_text(sentence):
    """
    Function to clean a sentence in German.
    """
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Remove special characters and punctuation (except numbers and letters)
    sentence = re.sub(r"[^a-zA-ZäöüÄÖÜß0-9\s]", "", sentence)
    
    # Tokenize and lemmatize using spaCy
    doc = nlp(sentence)
    sentence = " ".join([token.lemma_ for token in doc if not token.is_stop])
    
    # Remove extra spaces
    sentence = re.sub(r"\s+", " ", sentence).strip()
    
    return sentence

# Load dataset
data_path = "data/raw/deu_mixed-typical_2011_10K-sentences.txt"
data = pd.read_csv(data_path, delimiter="\t", names=["ID", "Sentence"], dtype={"ID": int, "Sentence": str})

# Apply cleaning
print("Cleaning data...")
data["Cleaned_Sentence"] = data["Sentence"].apply(clean_text)

# Save cleaned dataset
output_path = "data/processed/sentences_cleaned.csv"
data.to_csv(output_path, index=False)
print(f"Cleaned file saved at: {output_path}")