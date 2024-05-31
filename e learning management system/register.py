from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # TO DO: validate and store the user data in a database
        return 'Registration successful!'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)