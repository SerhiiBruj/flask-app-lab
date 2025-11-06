from flask import render_template, request
from . import users 

@users.route('/hi/<string:name>')
def greetings(name):
    age = request.args.get("age", None, type=int)
    return render_template('users/hi.html', name=name, age=age, title="Вітання")

@users.route('/admin')
def admin():
    # Редірект на /users/hi/Administrator?age=45
    return redirect(url_for('users.greetings', name='Administrator', age=45))