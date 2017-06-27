from flask import Flask, session, render_template, redirect, url_for, request
from app import app
from app import controllers 

@app.route('/')
@app.route('/index')
def index():
    if 'user' in session:
        return render_template("index.html",user=session['user'])
    else:
        return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = controllers.get_user_account_with_login(request.form['username'], request.form['password'])
        if (user is not None):
            session['user'] = user
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password. Please try again.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user', None)
   return redirect(url_for('index'))

@app.route('/callHistory')
def call_history():
    if 'user' not in session:
        #redirect the user if they aren't logged in
        return redirect(url_for('index'))
    call_history = controllers.get_user_call_history(session['user'])
    if call_history is None:
        error = "You have yet to make a call with Video Chat. Return to the <a href='/index>homepage</a> to learn how to make your first call!"
        return render_template('callHistory.html', error=error)
    else:
        return render_template('callHistory.html', user=session['user']['username'], calls=call_history)
