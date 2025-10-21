import sqlite3

class Database:
    def __init__(self, db_name="monitor_results.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            host TEXT,
            port INTEGER,
            status TEXT,
            latency REAL,
            timestamp TEXT
        )''')
        self.conn.commit()

    def insert_result(self, host, port, status, latency, timestamp):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO results (host, port, status, latency, timestamp) VALUES (?, ?, ?, ?, ?)",
                       (host, port, status, latency, str(timestamp)))
        self.conn.commit()

    def fetch_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT host, port, status, latency, timestamp FROM results")
        return cursor.fetchall()
