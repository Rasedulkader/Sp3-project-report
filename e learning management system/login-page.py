from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # Here you can add your logic for handling the login
    # For example, you can check if the username and password are correct
    # and then redirect the user to a different page
    return 'password saved'

if __name__ == '__main__':
    app.run(debug=True)