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
def hello_world():
    curr = mydb.cursor()
    curr.execute('select * from tasks')
    rows = curr.fetchall()

    return render_template('index.html', tasks = rows)

@app.route('/add/<name>')
def add_task(name):
    query_task = ("INSERT INTO tasks "
               "(name) "
               "VALUES (%s)")

    data_task = (name,)

    cursor = mydb.cursor()
    cursor.execute(query_task, data_task)
    task_no = cursor.lastrowid

    return "added baby!"
    

