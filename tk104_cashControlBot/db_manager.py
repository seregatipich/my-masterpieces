import sqlite3


def first_start_handler():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER UNIQUE, userName TEXT)')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS expenses (exp_id INTEGER UNIQUE PRIMARY KEY, id INTEGER, '
        'date TEXT, amount INTEGER, name TEXT, foreign key (id) references users(id))'
    )
    cursor.close()
    conn.close()


def save_user(user_id):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO users (id) VALUES ({user_id})')
    conn.commit()
    cursor.close()


def expense_handler(expense_name: str, expense_date: str, expense_amount: int):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    sqlite_insert_query = f'INSERT INTO expenses(name, date, amount) ' \
                          f'VALUES ({expense_name}, {expense_date}, {expense_amount});'
    cursor.execute(sqlite_insert_query)
    conn.commit()
    cursor.close()
