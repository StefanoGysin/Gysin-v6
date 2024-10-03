# src/core/knowledge_base.py
import sqlite3

class KnowledgeBase:
    def __init__(self):
        self.conn = sqlite3.connect('data/knowledge_base.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge
            (intent TEXT PRIMARY KEY, answer TEXT)
        ''')
        self.conn.commit()

    def has_answer(self, intent):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM knowledge WHERE intent = ?', (intent,))
        return cursor.fetchone() is not None

    def get_answer(self, intent):
        cursor = self.conn.cursor()
        cursor.execute('SELECT answer FROM knowledge WHERE intent = ?', (intent,))
        return cursor.fetchone()[0]

    def store_answer(self, intent, answer):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO knowledge (intent, answer) VALUES (?, ?)',
                       (intent, answer))
        self.conn.commit()