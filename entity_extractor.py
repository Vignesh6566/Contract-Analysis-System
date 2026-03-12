import spacy

class EntityExtractor:
    def __init__(self, model_name="en_core_web_sm"):
        try:
            self.nlp = spacy.load(model_name)
        except OSError:
            print(f"Model {model_name} not found. Attempting to download...")
            from spacy.cli import download
            download(model_name)
            self.nlp = spacy.load(model_name)

    def extract_entities(self, text):
        """Extracts PERSON, ORG, DATE, MONEY, and GPE entities."""
        doc = self.nlp(text)
        entities = []
        target_labels = {"PERSON", "ORG", "DATE", "MONEY", "GPE"}
        
        for ent in doc.ents:
            if ent.label_ in target_labels:
                entities.append({
                    "text": ent.text,
                    "label": ent.label_
                })
        return entities

if __name__ == "__main__":
    # Simple test
    extractor = EntityExtractor()
    test_text = "The obligor John Smith shall repay the loan to JPMorgan before 30 June 2026 for the amount of $10,000 in New York."
    results = extractor.extract_entities(test_text)
    for res in results:
        print(f"Entity: {res['text']} | Type: {res['label']}")
