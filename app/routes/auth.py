from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint("auth", __name__)

# Fixed: Use colons ":" for dictionaries and commas between items
USER_CREDENTIALS = {
    'username': 'admin',
    'password': '1234'
}

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Fixed: Access dict values with square brackets [] not parentheses ()
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash('Login Successful', 'success')
            # Typically you'd redirect here, e.g., redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out", 'info')
    return redirect(url_for('auth.login'))
