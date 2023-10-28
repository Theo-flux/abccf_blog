from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "abcctf blog platform"


if __name__ == "__main__":
    app.run(debug=True)
