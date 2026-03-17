from app import create_app, db
from app.models import Task

import os
print(f"Current Working Directory: {os.getcwd()}")


app = create_app()

# Corrected typo: 'wtih' changed to 'with'
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
