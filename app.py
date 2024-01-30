from flask import Flask , render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

#Routing
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact us.html')

@app.route('/user/<username>')
def user(username):
    return f'Hello, {username}!'

# Form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Thank you, {name}! We received your submission with email: {email}'
    return render_template('submissionform.html')