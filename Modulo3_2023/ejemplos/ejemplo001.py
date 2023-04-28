from flask import Flask

# La variable __name__ almacena el nombre del archivo actual
app = Flask(__name__)
print("resultado:"+__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()