from flask import Blueprint, render_template, request, make_response,redirect, url_for,session, flash 

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/404')
def NotFound():
    return render_template('404.html')

