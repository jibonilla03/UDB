from flask import Flask, render_template
import random
import datetime
import requests
import contacto

app = Flask(__name__)

url = "https://api.npoint.io/88bcfeb4049263321a59"
response = requests.get(url)
datos_agenda = response.json()
lista_contactos = []

@app.route("/agenda/<numero>")
def ver_agenda():
    for contacto in datos_agenda():


    return render_template("agenda_contactos.html", datos_agenda=datos_agenda)

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