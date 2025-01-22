from collections import defaultdict

def compare_ner_results(text, ner_results):
    """
    Compare the results of NER tools word by word.

    Args:
        text (str): The input text.
        ner_results (dict): NER results from multiple tools.

    Returns:
        dict: Comparison of NER results with word-level annotations.
    """
    comparison = defaultdict(dict)
    for tool_name, entities in ner_results.items():
        for entity in entities:
            if tool_name == "Hugging Face (BERT)":
                word = text[entity["start"] : entity["end"]]
                label = entity["entity"]
                comparison[word][tool_name] = label
            else:
                word = text[entity[1] : entity[2]]
                label = entity[3]
                comparison[word][tool_name] = label
    return comparison

def display_comparison(comparison):
    """
    Display the word-by-word comparison of NER results.

    Args:
        comparison (dict): Comparison dictionary with NER results.
    """
    print(f"{'Word':<30}{'spaCy':<30}{'Hugging Face (BERT)':<30}")
    print("=" * 90)
    for word, tool_results in comparison.items():
        spacy_label = tool_results.get("spaCy", "N/A")
        bert_label = tool_results.get("Hugging Face (BERT)", "N/A")
        print(f"{word:<30}{spacy_label:<30}{bert_label:<30}")

def extract_and_display_organizations(comparison):
    """
    Extract and display tokens identified as organizations (ORG) by at least one NER tool.

    Args:
        comparison (dict): Comparison dictionary with NER results.

    Returns:
        list: List of tokens identified as organizations.
    """
    organizations = []
    print(f"{'Token':<30}{'spaCy':<30}{'Hugging Face (BERT)':<30}")
    print("=" * 90)
    for word, tool_results in comparison.items():
        # Check if the token is labeled as 'ORG' by any model
        if "ORG" in tool_results.values():
            spacy_label = tool_results.get("spaCy", "N/A")
            bert_label = tool_results.get("Hugging Face (BERT)", "N/A")
            print(f"{word:<30}{spacy_label:<30}{bert_label:<30}")
            organizations.append(word)

    print("\nTokens identified as organizations by at least one model:")
    print(organizations)
    return organizations
