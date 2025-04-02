from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Set up the Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'siddiquiw100@gmail.com'  
app.config['MAIL_PASSWORD'] = 'Wali2003'  

mail = Mail(app)

# Simple in-memory user storage 
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    if email not in users:
        users[email] = None  # User is signed up, but no journal entry yet
        return redirect(url_for('home'))
    return 'User already signed up.'

@app.route('/submit_entry', methods=['POST'])
def submit_entry():
    email = request.form['email']
    entry = request.form['entry']
    
    # Send notification email to you
    send_notification(email)
    
    return 'Your journal entry has been received. Thank you!'

def send_notification(user_email):
    msg = Message('New Journal Entry Submitted', sender='siddiquiw100@gmail.com', recipients=['siddiquiw100@gmail.com'])
    msg.body = f"User {user_email} has submitted a journal entry. Please review it."
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug=True)