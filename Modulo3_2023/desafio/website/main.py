from flask import Flask, render_template
import random

app = Flask(__name__)

numero_aleatorio = random.randint(0, 9)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/adivinar/<num>")
def comparar_numeros(num):
    if int(num) == numero_aleatorio:
        return render_template("winner.html")
    elif int(num)  > numero_aleatorio:
        return render_template("loser.html")
    else:
        return render_template("loser.html")



if __name__ == "__main__":
    app.run()