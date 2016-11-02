from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Please click the login url below<br><a href = '/login'></b>click here to enter</b></a>" 

         
@app.route('/success_login')
def success_login():
    return "Welcome Login !"  

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success_login'))
    return render_template('login.html', error=error)




if __name__ == '__main__':
   app.run(debug = True)
