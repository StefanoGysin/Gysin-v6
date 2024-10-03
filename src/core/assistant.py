# src/core/assistant.py
from .knowledge_base import KnowledgeBase
from .nlp_processor import NLPProcessor

class Assistant:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.nlp_processor = NLPProcessor()

    def process_input(self, user_input):
        intent = self.nlp_processor.analyze_intent(user_input)
        if self.knowledge_base.has_answer(intent):
            return self.knowledge_base.get_answer(intent)
        else:
            answer = self.query_chatgpt(user_input)
            self.knowledge_base.store_answer(intent, answer)
            return answer

    def query_chatgpt(self, query):
        # Implementar a lógica de consulta ao ChatGPT aqui
        pass