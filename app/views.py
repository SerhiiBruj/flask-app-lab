from flask import Blueprint, render_template, request, make_response,redirect, url_for,session, flash 
from .forms import ContactForm
import logging

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('resume.html', title="Резюме Сергія")

@main.route('/resume')
def resume():
    return render_template('resume.html', title="Резюме Сергія")

logging.basicConfig(filename='contact.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        logging.info(f"Contact form: Name={name}, Email={email}, Message={message}")

        flash(f"Дякуємо, {name}! Ваше повідомлення успішно надіслано.", "success")
        return redirect(url_for('main.contact'))

    elif request.method == 'POST':
        flash("Будь ласка, виправте помилки у формі.", "error")

    return render_template('contact.html', form=form, title="Контактна форма")


@main.route('/admin')
def admin():
    return redirect(url_for('users.greetings', name='Administrator', age=45))



