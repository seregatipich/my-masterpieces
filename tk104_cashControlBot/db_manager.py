import sqlite3


class Dbconnection:
    def __enter__(self):
        self.conn = sqlite3.connect('bot.db')
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


def first_start_handler():
    with Dbconnection() as db:
        conn, cursor = db
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER UNIQUE PRIMARY KEY, userName TEXT)')
        conn.commit()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS expenses (exp_id INTEGER UNIQUE PRIMARY KEY, id INTEGER, '
            'date TEXT, amount INTEGER, name TEXT, foreign key (id) references users(id))'
        )
        conn.commit()
        return True

def save_user(user_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    try:
        cursor.execute(f'INSERT INTO users (id) VALUES ({user_id})')
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.commit()
        cursor.close()


def expense_handler(expense_name: str, expense_date: str, expense_amount: int, user_id: int):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    params = (user_id, expense_date, expense_amount, expense_name)
    try:
        cursor.execute(f'INSERT INTO expenses (id, date, amount, name) VALUES (?, ?, ?, ?)', params)
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.commit()
        cursor.close()
