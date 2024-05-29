# moderationLogs.py (Python)

```python
import sqlite3
from datetime import datetime

class ModerationLogs:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS moderation_logs (
                                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER NOT NULL,
                                mod_id INTEGER NOT NULL,
                                action TEXT NOT NULL,
                                reason TEXT,
                                timestamp TEXT NOT NULL
                                )''')
        self.conn.commit()

    def log_action(self, user_id, mod_id, action, reason):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''INSERT INTO moderation_logs (user_id, mod_id, action, reason, timestamp)
                                VALUES (?, ?, ?, ?, ?)''', (user_id, mod_id, action, reason, timestamp))
        self.conn.commit()

    def get_logs(self):
        self.cursor.execute('''SELECT * FROM moderation_logs''')
        logs = self.cursor.fetchall()
        return logs

    def get_logs_by_user(self, user_id):
        self.cursor.execute('''SELECT * FROM moderation_logs WHERE user_id = ?''', (user_id,))
        logs = self.cursor.fetchall()
        return logs

    def get_logs_by_mod(self, mod_id):
        self.cursor.execute('''SELECT * FROM moderation_logs WHERE mod_id = ?''', (mod_id,))
        logs = self.cursor.fetchall()
        return logs

    def close_connection(self):
        self.conn.close()
```
