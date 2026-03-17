from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

# The Blueprint name 'tasks' must match the first part of url_for('tasks.xxxx')
tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
        
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/add', methods=["POST"])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    else:
        flash('Task title cannot be empty', 'danger')
        
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
def toggle_status(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    task = db.session.get(Task, task_id)
    
    if task:
        # UPDATED LOGIC: Pending -> Working -> Completed -> Pending
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Completed"
        else:
            task.status = "Pending"
            
        db.session.commit()
    else:
        flash('Task not found', 'error')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))
        
    task = db.session.get(Task, task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted!', 'success')
    else:
        flash('Task not found', 'danger')
        
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    try:
        db.session.query(Task).delete()
        db.session.commit()
        flash('All tasks cleared!', 'info')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while clearing tasks.', 'danger')

    return redirect(url_for('tasks.view_tasks'))
