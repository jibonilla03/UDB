from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/invitado/<nombre>")
def ver_json(nombre):
    # 1. Para obtener los datos de un servicio necesitamos leer la documentacion
    url = f"https://api.genderize.io/?name={nombre}"
    # 2. Obtener el response haciendo uso de la URL
    response = requests.get(url)
    #print(response)
    #print(response.status_code)
    datos = response.json()
    nombre = datos.get("name") # datos["name"]
    genero = datos.get("gender")
    if genero == "male":
        genero = "Masculino"
    else:
        genero = "Femenino"

    probabilidad = datos.get("probability")
    return render_template("invitado.html", nombre=nombre, genero=genero, probabilidad=f"{probabilidad}%")

@app.route("/")
def inicio():
    aleatorio = random.randint(20,100)
    anio = datetime.datetime.now()
    return render_template("index.html", numero_aleatorio = aleatorio, anio = anio.year)


if __name__ == "__main__":
    app.run()