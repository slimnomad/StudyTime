from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Study Time</h1><p>Your AI-powered study planner</p>'

if __name__ == '__main__':
    app.run(debug=True)
