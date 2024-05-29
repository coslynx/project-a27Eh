# databaseIntegration.py (Python)

import sqlite3

class DatabaseIntegration:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            warnings INTEGER DEFAULT 0,
                            last_action TEXT
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS moderation_logs (
                            log_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            action TEXT,
                            timestamp TEXT,
                            FOREIGN KEY (user_id) REFERENCES users(user_id)
                            )''')
        self.conn.commit()

    def add_user(self, user_id, username):
        self.cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
        self.conn.commit()

    def get_user_warnings(self, user_id):
        self.cursor.execute('SELECT warnings FROM users WHERE user_id = ?', (user_id,))
        return self.cursor.fetchone()[0]

    def update_user_warnings(self, user_id, new_warnings):
        self.cursor.execute('UPDATE users SET warnings = ? WHERE user_id = ?', (new_warnings, user_id))
        self.conn.commit()

    def log_moderation_action(self, user_id, action, timestamp):
        self.cursor.execute('INSERT INTO moderation_logs (user_id, action, timestamp) VALUES (?, ?, ?)', (user_id, action, timestamp))
        self.conn.commit()

    def get_moderation_logs(self, user_id):
        self.cursor.execute('SELECT * FROM moderation_logs WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()