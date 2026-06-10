import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import Task

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-for-study-time'  # In production, use a proper secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'study_time.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

# Task routes
@app.route('/tasks')
def task_list():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('tasks/index.html', tasks=tasks)

@app.route('/tasks/new', methods=['GET', 'POST'])
def task_create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        difficulty = int(request.form['difficulty'])
        task = Task(title=title, description=description, difficulty=difficulty)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('task_list'))
    return render_template('tasks/form.html')

@app.route('/tasks/<int:id>/edit', methods=['GET', 'POST'])
def task_update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.difficulty = int(request.form['difficulty'])
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('task_list'))
    return render_template('tasks/form.html', task=task)

@app.route('/tasks/<int:id>/delete', methods=['POST'])
def task_delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('task_list'))

@app.route('/tasks/<int:id>/toggle', methods=['POST'])
def task_toggle(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    status = 'completed' if task.completed else 'marked as incomplete'
    flash(f'Task {status}!', 'success')
    return redirect(url_for('task_list'))

# CLI command to initialize the database
@app.cli.command('init-db')
def init_db():
    """Initialize the database."""
    db.create_all()
    print('Database initialized.')

if __name__ == '__main__':
    app.run(debug=True)