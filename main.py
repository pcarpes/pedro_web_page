from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)