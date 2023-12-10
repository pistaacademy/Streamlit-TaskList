import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS taskstable(task_doer TEXT, task_name TEXT, task_status TEXT, task_due_date DATE)')

def add_data(task_doer, task_name, task_status, task_due_date):
    c.execute('INSERT INTO taskstable(task_doer, task_name, task_status, task_due_date) VALUES (?,?,?,?)',(task_doer, task_name, task_status, task_due_date))
    conn.commit()

def view_all_tasks():
    c.execute('SELECT * FROM taskstable')
    data = c.fetchall()
    return data