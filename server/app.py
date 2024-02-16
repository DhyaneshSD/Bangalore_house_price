from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_world():
    return "hello World"

@app.route('/production')
def production():
    return "this is production page"


if __name__ == "__main__":
    app.run()