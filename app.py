from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
#calls weather from a script that pulls data from openweather API
from weather import temp

app = Flask(__name__)
app.config['SQLALCHEMY_BASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

class Shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    now = datetime.datetime.now() # current date and time
    date_time = now.strftime("%A, %B %W %Y")
    current_time = now.strftime("%I:%M %p")
    #show all todos
    todo_list = Todo.query.all()
    menu_list = Menu.query.all()
    shopping_list = Shopping.query.all()
    return render_template('base.html', todo_list=todo_list, shopping_list=shopping_list, menu_list=Menu.query.all(), date_time = date_time, current_time = current_time, temp=temp)

     

@app.route('/add', methods=["POST"])
def add():
    #add new item
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    new_todo = Todo(title="todo 1", complete=False)
    db.session.add(new_todo)
    db.session.commit()
    #debug and port need to be changed in production
    app.run(debug=True, port=5000, host='0.0.0.0')