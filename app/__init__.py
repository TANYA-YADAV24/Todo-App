from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the database object
db = SQLAlchemy()

def create_app():
    # 1. Define the root directory (todo-app folder)
    # Ensure this points to the folder containing /templates
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    template_dir = os.path.join(root_dir, 'templates')
    static_dir = os.path.join(root_dir, 'static')

    # 2. Initialize Flask pointing to the absolute paths
    app = Flask(__name__, 
                template_folder=template_dir, 
                static_folder=static_dir)

    # 3. Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(root_dir, 'todo.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 4. Initialize DB
    db.init_app(app)

    # 5. Debugging logs (already look good in your output)
    print(f"--- PROJECT ROOT: {root_dir}")
    if not os.path.exists(template_dir):
        print(f"--- ERROR: Templates folder NOT FOUND at {template_dir}")

    # 6. Register Blueprints 
    # IMPORTANT: Ensure tasks_bp = Blueprint('tasks', __name__) 
    # without a template_folder arg in task.py
    from app.routes.auth import auth_bp
    from app.routes.task import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    # 7. Create database tables
    with app.app_context():
        from app.models import User, Task
        db.create_all()
        print("--- DATABASE: Tables created successfully!")

    return app
