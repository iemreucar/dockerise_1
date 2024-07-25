from flask import Flask, render_template

app = Flask(__name__)

@app.route('/service1')
def call_service1():
    return "Data from Service1"

@app.route('/service2')
def call_service2():
    return "Data from Service2"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
