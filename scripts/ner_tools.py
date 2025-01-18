import spacy
from transformers import pipeline

def load_ner_tools(language="de"):
    """
    Load different NER tools/models for the specified language.
    
    Args:
        language (str): Language code for the models (e.g., 'de' for German, 'en' for English).
    
    Returns:
        dict: A dictionary of NER tools with their names as keys.
    """
    if language == "de":
        tools = {
            "spaCy": spacy.load("de_core_news_sm"),
            "Hugging Face (BERT)": pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-german"),
        }
    elif language == "en":
        tools = {
            "spaCy": spacy.load("en_core_web_sm"),
            "Hugging Face (BERT)": pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english"),
        }
    else:
        raise ValueError(f"Unsupported language: {language}")
    
    return tools

def apply_ner_tools(text, tools):
    """
    Apply NER tools to the given text.

    Args:
        text (str): The input text (article content).
        tools (dict): A dictionary of loaded NER tools.

    Returns:
        dict: A dictionary with tool names as keys and their NER results as values.
    """
    results = {}
    for tool_name, tool in tools.items():
        if tool_name == "spaCy":
            doc = tool(text)
            entities = [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
        elif tool_name == "Hugging Face (BERT)":
            entities = tool(text)
        else:
            entities = []
        results[tool_name] = entities
    return results
