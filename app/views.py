from flask import Blueprint, render_template, request, make_response,redirect, url_for,session, flash

main = Blueprint('main', __name__, template_folder='templates')
USER_DATA = {
    "admin": "12345",
    "serhii": "qwerty"
}
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
    return redirect(url_for('users.greetings', name='Administrator', age=45))



