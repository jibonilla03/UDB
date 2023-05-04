from flask import Flask

app = Flask(__name__)


@app.route("/") # http://127.0.0.1:5000
def home():
    return "<p>Bienvenido a Flask 2023</p>"


@app.route("/lista_empleados") # http://127.0.0.1:5000/lista_empleados
def listar_empleados():
    return "<h1> Alejandro | Sarai | Carlos | Dennis </h1>"

# Vamos a recibir e parametro <id> y lo vamos a utilizar en la funcion ver_empleado
# Los parametros se reciben haciendo uso de los signos < (menor que) y > (mayor que)
@app.route("/empleado/<id>") # http://127.0.0.1:5000/lista_empleados/12
def ver_empleado(id):
    # Podriamos hacer un select * from empleados where id = id
    return f"Bienvenido empleado con id: {id}"

# Podemos recibir mas de un parametro enviado a traves de la URL
# Tambien podemos definir el tipo de dato de dichos parametros
@app.route("/empleado/<nombre>/<edad>") #http://127.0.0.1:5000/empleado/Mayra/27
def ver_info_empleado(nombre, edad):
    return f"Bienvenido {nombre}, tu edad es: {edad}"

# Ventajas de utilizar Debug en la applicacion:
# 1. Permite ver las actualizaciones en el codigo sin reiniciar el servidor
# 2. Nos ayuda a identificar errores en el codigo a los programadores fuente a traves de un traza del mismo error
# 3. Nos permite usar la consola desde la web para poder identificar el error a corregir. Aca utilizamos el pin de seguridad

if __name__ == "__main__":
    app.run()