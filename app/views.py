from flask import Flask, session, render_template, redirect, url_for, request, abort
from app import app
from app import controllers 

@app.errorhandler(404)
def page_not_found(error):
    if 'user' in session:
        return render_template('404.html',user=session['user']), 404
    else:
        return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def index():
    if 'user' in session:
        return render_template("index.html",user=session['user'])
    else:
        return render_template("index.html")

@app.route('/call/<room_name>/<call_id>', methods = ['GET'])
def call(room_name, call_id):
    if 'user' in session:
        return render_template("index.html", user=session['user'], room_name=room_name, call_id=call_id)
    else: 
        return render_template("index.html", room_name=room_name, call_id=call_id)

@app.route('/login', methods=['GET','POST'])
def login():
    if 'user' in session:
        #redirect the user if they are already logged in
        return redirect(url_for('index'))
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
    if call_history == []:
        error = True
        return render_template('callHistory.html', user=session['user'], error=error)
    else:
        return render_template('callHistory.html', user=session['user'], calls=call_history)

@app.route('/logCall/<user_id>/<room_name>', methods = ['GET'])
def log_call(user_id, room_name):
    call_id = controllers.log_new_call(user_id, room_name)
    return call_id

@app.route('/logGuestInActiveCall/<guest_user_id>/<call_id>', methods = ['GET'])
def log_guest_in_active_call(guest_user_id, call_id):
    no_error = controllers.update_guest_id_in_an_active_call(call_id, guest_user_id)
    if not no_error:
        #MAKE error that the call you're trying to access doesn't exist apparent
        abort(500)
    else:
        return call_id
