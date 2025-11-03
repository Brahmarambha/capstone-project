from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Your Capstone Project Web App is Running Successfully 🎉"

if __name__ == '__main__':
    app.run(debug=True)
