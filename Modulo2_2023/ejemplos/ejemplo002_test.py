from ejemplo002 import Medicamento

# Al crear un objeto de la clase, lo primero que se invoca es el constructor
dolofin_antigripal = Medicamento("dolofin_mk", "Para dolores de cabeza")
print(dolofin_antigripal.nombre_generico)
print(dolofin_antigripal.descripcion)
dolofin_antigripal.precio = 0.20

ibuprofeno = Medicamento("dolofin_mk", "Para otros dolores")
print(ibuprofeno.nombre_generico)
print(ibuprofeno.descripcion)
print(ibuprofeno.precio)

# Guardar en la base de datos el objeto dolofin_antigripal y el objeto ibuprofeno