from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'procv-builder-secret-key-2025'

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates')
def templates():
    return render_template('templates.html')

@app.route('/builder')
def builder():
    return render_template('builder.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    # In a real application, you would save this to a database or send an email
    return jsonify({'success': True, 'message': 'Message received successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
