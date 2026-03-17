from app import db
from datetime import datetime, timezone

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    # Automatically tracks when the task was created
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # This ensures your 'created_at' is set when you make a new task
    def __init__(self, title, status='Pending'):
        self.title = title
        self.status = status
        self.created_at = datetime.now(timezone.utc)
