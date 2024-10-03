# src/core/nlp_processor.py
import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_intent(self, text):
        doc = self.nlp(text)
        # Implementar lógica de análise de intenção aqui
        return text.lower()  # Simplificação para exemplo