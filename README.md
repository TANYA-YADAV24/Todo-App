# Flask Task Manager (Todo-App)

A secure Task Management System built with **Flask Blueprints**. This project features a modular architecture, session-based authentication, and real-time user feedback via flash messaging.

## 🚀 Features
* **Modular Architecture**: Uses Flask Blueprints for clean code organization.
* **Secure Authentication**: Session-based login and logout system.
* **User Feedback**: Integrated Flask Flash Messaging for success and error notifications.
* **Session Management**: Secure client-side sessions to track logged-in users. 

## 🛠️ Tech Stack
* **Backend**: Python 3.x, Flask
* **Frontend**: Jinja2 Templates, HTML5, CSS3
* **Security**: Flask-Session Management

## 📂 Project Structure


├── app.py              # Main application factory
├── auth.py             # Authentication Blueprint (Login/Logout)
├── templates/          # HTML files
│   ├── login.html      # Login page
│   └── index.html      # Main todo dashboard
├── static/             # CSS and JavaScript files
└── requirements.txt    # Project dependencies


⚙️ Installation & Setup

   1. Clone the repository:
   
   git clone https://github.com
   cd Todo-App
   
   2. Create a virtual environment:
   
   python -m venv venv# Windows: venv\Scripts\activate# Mac/Linux: source venv/bin/activate
   
   3. Install dependencies:
   
   pip install Flask
   
   4. Set a Secret Key:
   Open app.py and ensure you have a SECRET_KEY defined:
   
   app.config['SECRET_KEY'] = 'your_super_secret_random_key'
   
   5. Run the application:
   
   python app.py
   
   
🔑 Default Credentials
For testing purposes, the app uses these hardcoded credentials:

* Username: admin
* Password: 1234

📝 License
Distributed under the MIT License.





