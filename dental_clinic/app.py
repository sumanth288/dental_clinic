from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__, template_folder='.')
app.secret_key = os.urandom(24)  # Needed for flash messages

# Flask-Mail configuration (Gmail SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sumanthreddy1200@gmail.com'  # <-- Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'Sumanth@12'     # <-- Replace with your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'sumanthreddy695@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        # Get form data
        data = request.form
        subject = 'New Appointment Request'
        body = f"""
        New appointment request from {data.get('firstName', '')} {data.get('lastName', '')}
        Email: {data.get('email', '')}
        Phone: {data.get('phone', '')}
        Preferred Date: {data.get('date', '')}
        Preferred Time: {data.get('time', '')}
        Service: {data.get('service', '')}
        Message: {data.get('message', '')}
        """
        try:
            msg = Message(subject, recipients=['sumanthreddy695@gmail.com'], body=body)
            mail.send(msg)
            flash('Appointment request sent successfully!', 'success')
        except Exception as e:
            flash('Failed to send appointment request. Please try again later.', 'danger')
        return redirect(url_for('appointment'))
    return render_template('appointment.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        subject = f"Contact Form: {data.get('subject', 'No Subject')}"
        body = f"""
        New contact message from {data.get('name', '')}
        Email: {data.get('email', '')}
        Subject: {data.get('subject', '')}
        Message: {data.get('message', '')}
        """
        try:
            msg = Message(subject, recipients=['sumanthreddy112000@gmail.com'], body=body)
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('Failed to send your message. Please try again later.', 'danger')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 