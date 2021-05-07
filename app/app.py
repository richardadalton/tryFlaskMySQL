import mysql.connector
from flask import Flask, render_template

app=Flask(__name__)

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="secret",
    database="todos"
)


@app.route('/')
def index():
    curr = mydb.cursor()
    curr.execute('select * from tasks')
    rows = curr.fetchall()
    return render_template('index.html', tasks = rows)


@app.route('/add/<name>')
def add_task(name):
    task_query = "INSERT INTO tasks (name) VALUES (%s)"
    task_data = (name,)

    cursor = mydb.cursor()
    cursor.execute(task_query, task_data)
    task_no = cursor.lastrowid
    mydb.commit()

    return f"added {task_no}"
