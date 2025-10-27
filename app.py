from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('resume.html', title="Резюме Сергія")

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Резюме Сергія")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Контакти")

if __name__ == '__main__':
    app.run(debug=True)
