from flask import Blueprint, render_template

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
