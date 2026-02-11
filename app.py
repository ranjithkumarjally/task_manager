
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import db
from models.task import Task, Priority

app = Flask(__name__)

# Environment-based configuration for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'mysql+pymysql://root:password@localhost:3306/taskmanager'  # Fallback for local development
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,  # Verify connections before using
    'pool_recycle': 3600,   # Recycle connections after 1 hour
}
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

db.init_app(app)

with app.app_context():
    db.create_all()

# Health check endpoint for ALB
@app.route('/health')
def health_check():
    try:
        # Test database connection
        db.session.execute(db.text('SELECT 1'))
        return {'status': 'healthy', 'service': 'task-manager', 'database': 'connected'}, 200
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}, 503

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        deadline = request.form.get('deadline')

        if not title or not priority:
            flash('Title and priority are required!', 'danger')
            return redirect(url_for('index'))

        try:
            priority = Priority[priority.upper()]
        except KeyError:
            flash('Invalid priority selected!', 'danger')
            return redirect(url_for('index'))

        deadline_date = None
        if deadline:
            try:
                deadline_date = datetime.strptime(deadline, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid deadline format!', 'danger')
                return redirect(url_for('index'))

        new_task = Task(
            title=title,
            description=description,
            priority=priority,
            deadline=deadline_date
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('index'))

    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        deadline = request.form.get('deadline')

        if not title or not priority:
            flash('Title and priority are required!', 'danger')
            return redirect(url_for('edit_task', task_id=task_id))

        try:
            priority = Priority[priority.upper()]
        except KeyError:
            flash('Invalid priority selected!', 'danger')
            return redirect(url_for('edit_task', task_id=task_id))

        deadline_date = None
        if deadline:
            try:
                deadline_date = datetime.strptime(deadline, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid deadline format!', 'danger')
                return redirect(url_for('edit_task', task_id=task_id))

        task.title = title
        task.description = description
        task.priority = priority
        task.deadline = deadline_date
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash('Task status updated!', 'success')
    return redirect(url_for('index'))

@app.route('/filter')
def filter_tasks():
    priority = request.args.get('priority')
    status = request.args.get('status')
    query = Task.query

    if priority and priority in [p.value for p in Priority]:
        query = query.filter_by(priority=Priority[priority.upper()])
    if status == 'completed':
        query = query.filter_by(completed=True)
    elif status == 'incomplete':
        query = query.filter_by(completed=False)

    tasks = query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=False)

