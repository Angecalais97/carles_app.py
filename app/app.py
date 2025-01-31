from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "carles whish you a warming welcome to DevOps Easy Learning!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
