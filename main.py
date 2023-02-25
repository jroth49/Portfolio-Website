from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return render_template('header.html', username=name)

@app.route('/login')
def login():
    return 'LOGIN PAGE'

@app.route('/security')
def security():
    return 'Security Page'

@app.route('/admin')
def admin():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()

