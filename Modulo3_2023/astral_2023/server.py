from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html") # Este archivo lo va a buscar en la carpeta templates


if __name__ == "__main__":
    app.run()