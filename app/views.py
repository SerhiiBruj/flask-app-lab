from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('resume.html', title="Резюме Сергія")

@main.route('/resume')
def resume():
    return render_template('resume.html', title="Резюме Сергія")

@main.route('/contact')
def contact():
    return render_template('contact.html', title="Контакти")

@main.route('/admin')
def admin():
    # Редірект на /users/hi/Administrator?age=45
    return redirect(url_for('users.greetings', name='Administrator', age=45))