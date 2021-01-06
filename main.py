from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('main.html')

@app.route('/history/')
def render_history():
    return render_template('my_history.html')

@app.route('/contact/')
def render_contact():
    return render_template("contact.html")

@app.route('/work/')
def render_work():
    return render_template("work.html")

if __name__ == '__main__':
    app.run()
