from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Omega2 AI Paraphrasing Tool is Running!"

if __name__ == '__main__':
    app.run(debug=True)
