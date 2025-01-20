import spacy
from transformers import pipeline

def load_ner_tools(language="de"):
    tools = {}
    try:
        if language == "de":
            tools = {
                "spaCy": spacy.load("de_core_news_sm"),
                "Hugging Face (BERT)": pipeline("ner", model="deepset/gbert-large"),
            }
        elif language == "en":
            tools = {
                "spaCy": spacy.load("en_core_web_sm"),
                "Hugging Face (BERT)": pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english"),
            }
    except Exception as e:
        print(f"Error loading NER tools: {e}")
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
