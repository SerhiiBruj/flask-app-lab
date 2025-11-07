from flask import render_template, request, make_response,redirect, url_for,session, flash
from . import users 
from .forms import LoginForm


USER_DATA = {
    "admin": "12345",
    "serhii": "qwerty"
}
@users.route('/hi/<string:name>')
def greetings(name):
    age = request.args.get("age", None, type=int)
    return render_template('users/hi.html', name=name, age=age, title="Вітання")

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data

        if username in USER_DATA and password == USER_DATA[username]:
            session['user'] = username
            flash(f"Успішний вхід як {username}. Remember: {remember}", "success")
            return redirect(url_for('users.profile'))
        else:
            flash("Невірні дані для входу!", "danger")
            return redirect(url_for('users.login'))  

    return render_template('users/login.html', form=form)

@users.route('/logout')
def logout():
    session.pop('user', None)
    flash("Ви вийшли із системи!", "success")
    return redirect(url_for('users.login'))


@users.route('/profile', methods=['GET', 'POST'])
def profile():
    user = session.get('user')
    if not user:
        flash("Будь ласка, увійдіть у систему!", "error")
        return redirect(url_for('users.login'))

    resp = make_response(render_template('users/profile.html', user=user, cookies=request.cookies, title="Профіль"))

    if request.method == 'POST' and 'add_cookie' in request.form:
        key = request.form.get('key')
        value = request.form.get('value')
        max_age = request.form.get('max_age')

        if key and value:
            try:
                max_age = int(max_age) if max_age else None
            except ValueError:
                max_age = None
            resp.set_cookie(key, value, max_age=max_age)
            flash(f"Cookie '{key}' додано успішно!", "success")
        else:
            flash("Будь ласка, введіть ключ і значення!", "error")

    if request.method == 'POST' and 'delete_cookie' in request.form:
        key = request.form.get('delete_key')
        if key in request.cookies:
            resp.delete_cookie(key)
            flash(f"Cookie '{key}' видалено!", "info")
        else:
            flash(f"Cookie '{key}' не знайдено!", "warning")

    if request.method == 'POST' and 'delete_all' in request.form:
        for k in request.cookies.keys():
            resp.delete_cookie(k)
        flash("Усі cookie видалено!", "info")

    return resp

@users.route('/set_theme/<theme>')
def set_theme(theme):
    if theme not in ['light', 'dark']:
        flash("Невідома тема!", "warning")
        return redirect(url_for('users.profile'))

    resp = make_response(redirect(url_for('users.profile')))
    session['theme'] = theme
    flash(f"Кольорова схема змінена на {theme}!", "success")
    return resp