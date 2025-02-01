from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the web application!"

@app.route('/download')
def download_file():
    return send_file('main.py', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)