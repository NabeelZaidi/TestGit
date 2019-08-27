from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"
@app.route("/hello")
def hello():
    return "{'name':'nabeel'}"
if __name__ == '__main__':
    app.run()
