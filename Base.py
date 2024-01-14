import sqlite3

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def add(self, word, describe):
        with self.connection:
            return self.cursor.execute('INSERT INTO all_words (Word, Describe) VALUES(?, ?)', (word, describe))

    def ret_description(self, word):
        with self.connection:
            return self.cursor.execute('SELECT Describe FROM all_words WHERE Word = ?', (word, )).fetchall()
