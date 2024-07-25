from flask import Flask, render_template

app = Flask(__name__)

@app.route('/service2')
def call_service2():
    return "Data from Service2"

@app.route('/service3')
def call_service3():
    return "Data from Service3"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
