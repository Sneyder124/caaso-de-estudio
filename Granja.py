import mysql.connector
import tkinter as tk
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ejercicio_caso_de_estudio_Phyton",
    password = ""
)
    
def insertar_registro(nombre, tipo, area_cultivo, rendimiento):
    cursor = db.cursor()
    sql = "INSERT INTO Cultivos_Granja ( nombre, tipo, area_cultivo, rendimiento) VALUES (%s, %s, %s, %s)"
    valores = ( nombre, tipo, area_cultivo, rendimiento)
    cursor.execute(sql, valores)
    db.commit()
    cursor.close()

def abrir_ventana_insertar_registro():
    def insertar_registro_auxiliar():
        entry_rendimiento= entry_area_rendimiento 
        nombre = entry_nombre.get()
        tipo = entry_tipo.get() 
        area_cultivo = float(entry_area_cultivo.get()) 
        rendimiento = float(entry_rendimiento.get()) 

        insertar_registro( nombre, tipo, area_cultivo, rendimiento)
        ventana_insertar_registro.destroy()

    ventana_insertar_registro = tk.Toplevel()
    ventana_insertar_registro.title("Insertar registro de cultivo")

    # Crear etiquetas y campos de entrada
    
    etiqueta_nombre = tk.Label(ventana_insertar_registro, text="Dame el nombre del cultivo:")
    etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5)

    entry_nombre = tk.Entry(ventana_insertar_registro)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_tipo = tk.Label(ventana_insertar_registro, text="Dame el tipo del cultivo:")
    etiqueta_tipo.grid(row=1, column=0, padx=10, pady=5)

    entry_tipo = tk.Entry(ventana_insertar_registro)
    entry_tipo.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_area_cultivo = tk.Label(ventana_insertar_registro, text="Dame el area sembrada del cultivo:")
    etiqueta_area_cultivo.grid(row=2, column=0, padx=10, pady=5)

    entry_area_cultivo = tk.Entry(ventana_insertar_registro)
    entry_area_cultivo.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_rendimiento = tk.Label(ventana_insertar_registro, text="Dame el rendimiento basandote en el area sembrada:")
    etiqueta_rendimiento.grid(row=3, column=0, padx=10, pady=5)

    entry_area_rendimiento = tk.Entry(ventana_insertar_registro)
    entry_area_rendimiento.grid(row=3, column=1, padx=10, pady=5)

    # Crear botón para guardar
    boton_guardar = tk.Button(ventana_insertar_registro, text="Guardar", command=insertar_registro_auxiliar)
    boton_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def insertar_registro1(Especie, raza , edad, peso):
    cursor = db.cursor()
    sql = "INSERT INTO Ganado_Granja ( Especie, raza, edad, peso) VALUES (%s, %s, %s, %s)"
    valores = ( Especie, raza, edad, peso)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close()

def abrir_ventana_insertar_registro1():
    def insertar_registro_auxiliar1():
        Especie = entry_Especie.get()
        raza = entry_raza.get() 
        edad = int(entry_edad.get()) 
        peso = float(entry_peso.get()) 

        insertar_registro1( Especie, raza, edad, peso)
        ventana_insertar_registro1.destroy()

    ventana_insertar_registro1 = tk.Toplevel()
    ventana_insertar_registro1.title("Insertar registro de ganado")

    # Crear etiquetas y campos de entrada
    
    etiqueta_Especie = tk.Label(ventana_insertar_registro1, text="Dame la especie del animal:")
    etiqueta_Especie.grid(row=0, column=0, padx=10, pady=5)

    entry_Especie = tk.Entry(ventana_insertar_registro1)
    entry_Especie.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_raza = tk.Label(ventana_insertar_registro1, text="Dame su raza:")
    etiqueta_raza.grid(row=1, column=0, padx=10, pady=5)

    entry_raza = tk.Entry(ventana_insertar_registro1)
    entry_raza.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_edad = tk.Label(ventana_insertar_registro1, text="Dame su edad:")
    etiqueta_edad.grid(row=2, column=0, padx=10, pady=5)

    entry_edad = tk.Entry(ventana_insertar_registro1)
    entry_edad.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_peso = tk.Label(ventana_insertar_registro1, text="Dame su peso:")
    etiqueta_peso.grid(row=3, column=0, padx=10, pady=5)

    entry_peso = tk.Entry(ventana_insertar_registro1)
    entry_peso.grid(row=3, column=1, padx=10, pady=5)

    # Crear botón para guardar
    boton_guardar = tk.Button(ventana_insertar_registro1, text="Guardar", command=insertar_registro_auxiliar1)
    boton_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def leer_registros():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Cultivos_Granja")
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)
    cursor.close()

def leer_registros1():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Ganado_Granja")
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)
    cursor.close()

def modificar_registro( id_cultivo, nombre, tipo, area_cultivo, rendimiento):
    cursor = db.cursor()
    sql = "UPDATE Cultivos_Granja SET nombre = %s, tipo = %s, area_cultivo = %s, rendimiento = %s WHERE id = %s"
    valores = (nombre, tipo, area_cultivo, rendimiento, id_cultivo)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close()

def abrir_ventana_modificar_registro():
    def modificar_registro_auxiliar():
        id_cultivo = int(entry_id_empleado.get())
        nombre = entry_nombre.get()
        tipo = entry_tipo.get() 
        area_cultivo = float(entry_area_cultivo.get()) 
        rendimiento = float(entry_rendimiento.get()) 

        modificar_registro(nombre, tipo, area_cultivo, rendimiento, id_cultivo)
        ventana_modificar_registro.destroy()

    ventana_modificar_registro = tk.Toplevel()
    ventana_modificar_registro.title("Modificar registro del cultivo")

    # Crear etiquetas y campos de entrada

    etiqueta_id_empleado = tk.Label(ventana_modificar_registro, text="ID del cultivo:")
    etiqueta_id_empleado.grid(row=0, column=0, padx=10, pady=5)

    entry_id_empleado = tk.Entry(ventana_modificar_registro)
    entry_id_empleado.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_nombre = tk.Label(ventana_modificar_registro, text="Dame el nombre del cultivo:")
    etiqueta_nombre.grid(row=1, column=0, padx=10, pady=5)

    entry_nombre = tk.Entry(ventana_modificar_registro)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_tipo = tk.Label(ventana_modificar_registro, text="Dame el tipo del cultivo:")
    etiqueta_tipo.grid(row=2, column=0, padx=10, pady=5)

    entry_tipo = tk.Entry(ventana_modificar_registro)
    entry_tipo.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_area_cultivo = tk.Label(ventana_modificar_registro, text="Dame el area sembrada del cultivo:")
    etiqueta_area_cultivo.grid(row=3, column=0, padx=10, pady=5)

    entry_area_cultivo = tk.Entry(ventana_modificar_registro)
    entry_area_cultivo.grid(row=3, column=1, padx=10, pady=5)

    etiqueta_rendimiento = tk.Label(ventana_modificar_registro, text="Dame el rendimiento basandote en el area sembrada:")
    etiqueta_rendimiento.grid(row=4, column=0, padx=10, pady=5)

    entry_rendimiento = tk.Entry(ventana_modificar_registro)
    entry_rendimiento.grid(row=4, column=1, padx=10, pady=5)

    # Crear botón para modificar
    boton_modificar = tk.Button(ventana_modificar_registro, text="Modificar", command=modificar_registro_auxiliar)
    boton_modificar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def modificar_registro1( Especie, raza, edad, peso, animal_id):
    cursor = db.cursor()
    sql = "UPDATE Ganado_Granja SET Especie = %s, raza = %s, edad = %s, peso = %s WHERE id = %s"
    valores = (Especie, raza, edad, peso, animal_id)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close()

def abrir_ventana_modificar_registro1():
    def modificar_registro_auxiliar1():
        animal_id = int(entry_animal_id.get())
        Especie = entry_Especie.get()
        raza = entry_raza.get() 
        edad = int(entry_edad.get()) 
        peso = float(entry_peso.get())

        modificar_registro(Especie, raza, edad, peso, animal_id)
        ventana_modificar_registro1.destroy()

    ventana_modificar_registro1 = tk.Toplevel()
    ventana_modificar_registro1.title("Modificar registro del cultivo")

    # Crear etiquetas y campos de entrada

    etiqueta_animal_id = tk.Label(ventana_modificar_registro1, text="ID del animal:")
    etiqueta_animal_id.grid(row=0, column=0, padx=10, pady=5)

    entry_animal_id = tk.Entry(ventana_modificar_registro1)
    entry_animal_id.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_Especie = tk.Label(ventana_modificar_registro1, text="Dame la especie del animal:")
    etiqueta_Especie.grid(row=0, column=0, padx=10, pady=5)

    entry_Especie = tk.Entry(ventana_modificar_registro1)
    entry_Especie.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_raza = tk.Label(ventana_modificar_registro1, text="Dame su raza:")
    etiqueta_raza.grid(row=1, column=0, padx=10, pady=5)

    entry_raza = tk.Entry(ventana_modificar_registro1)
    entry_raza.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_edad = tk.Label(ventana_modificar_registro1, text="Dame su edad:")
    etiqueta_edad.grid(row=2, column=0, padx=10, pady=5)

    entry_edad = tk.Entry(ventana_modificar_registro1)
    entry_edad.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_peso = tk.Label(ventana_modificar_registro1, text="Dame su peso:")
    etiqueta_peso.grid(row=3, column=0, padx=10, pady=5)

    entry_peso = tk.Entry(ventana_modificar_registro1)
    entry_peso.grid(row=3, column=1, padx=10, pady=5)


    # Crear botón para modificar
    boton_modificar = tk.Button(ventana_modificar_registro1, text="Modificar", command=modificar_registro_auxiliar1)
    boton_modificar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def eliminar_registro(cultivo_id):
    cursor = db.cursor()
    sql = "DELETE FROM Cultivos_Granja WHERE id = %s"
    valores = (cultivo_id,)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close() 

def abrir_ventana_eliminar_registro():
    def eliminar_registro_auxiliar():
        cultivo_id = int(cultivo_id.get()) 

        eliminar_registro(cultivo_id)
        ventana_eliminar_registro.destroy()

    ventana_eliminar_registro = tk.Toplevel()
    ventana_eliminar_registro.title("Eliminar registro")

    # Crear etiqueta y campo de entrada
    etiqueta_id_cultivo = tk.Label(ventana_eliminar_registro, text="Dame el id del cultivo:")
    etiqueta_id_cultivo.grid(row=0, column=0, padx=10, pady=5)

    entry_id_empleado = tk.Entry(ventana_eliminar_registro)
    entry_id_empleado.grid(row=0, column=1, padx=10, pady=5)

    # Crear botón para eliminar
    boton_eliminar = tk.Button(ventana_eliminar_registro, text="Eliminar", command=eliminar_registro_auxiliar)
    boton_eliminar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Aviso de confirmación
    messagebox.showwarning("¡Atención!", "¿Está seguro de que desea eliminar este registro? Esta acción es irreversible.")


def eliminar_registro1(animal_id):
    cursor = db.cursor()
    sql = "DELETE FROM Ganado_Granja WHERE id = %s"
    valores = (animal_id,)
    cursor.execute(sql, valores)
    db.commit()

    cursor.close() 

def abrir_ventana_eliminar_registro1():
    def eliminar_registro_auxiliar1():
        animal_id = int(animal_id.get()) 

        eliminar_registro1(animal_id)
        ventana_eliminar_registro1.destroy()

    ventana_eliminar_registro1 = tk.Toplevel()
    ventana_eliminar_registro1.title("Eliminar registro")

    # Crear etiqueta y campo de entrada
    etiqueta_animal_id = tk.Label(ventana_eliminar_registro1, text="Dame el id del animal:")
    etiqueta_animal_id.grid(row=0, column=0, padx=10, pady=5)

    entry_animal_id = tk.Entry(ventana_eliminar_registro1)
    entry_animal_id.grid(row=0, column=1, padx=10, pady=5)

    # Crear botón para eliminar
    boton_eliminar = tk.Button(ventana_eliminar_registro1, text="Eliminar", command=eliminar_registro_auxiliar1)
    boton_eliminar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Aviso de confirmación
    messagebox.showwarning("¡Atención!", "¿Está seguro de que desea eliminar este registro? Esta acción es irreversible.")

def crear_ventana_Administrar_Cultivos():
     ventana_Administrar_Cultivos = tk.Tk()
     ventana_Administrar_Cultivos.title("Menú Administrar Cultivos-Granja Ucundinamarca")

     etiqueta_leer_registros = tk.Label(ventana_Administrar_Cultivos, text="1.Leer registros de cultivo")
     etiqueta_leer_registros.grid(row=1, column=0, padx=30, pady=25)

     etiqueta_insertar_registro = tk.Label(ventana_Administrar_Cultivos, text="2.Insertar registro de cultivo")
     etiqueta_insertar_registro.grid(row=2, column=0, padx=30, pady=25)

     etiqueta_modificar_registro = tk.Label(ventana_Administrar_Cultivos, text="3.Modificar registro de cultivo")
     etiqueta_modificar_registro.grid(row=3, column=0, padx=30, pady=25)

     etiqueta_eliminar_registro = tk.Label(ventana_Administrar_Cultivos, text="4.Eliminar registro")
     etiqueta_eliminar_registro.grid(row=4, column=0, padx=30, pady=25)

     etiqueta_salir = tk.Label(ventana_Administrar_Cultivos, text="5.Salir")
     etiqueta_salir.grid(row=5, column=0, padx=30, pady=30)

    # Crear botones
     boton_leer_registros = tk.Button(ventana_Administrar_Cultivos, text="Leer", command=leer_registros)
     boton_leer_registros.grid(row=1, column=1, padx=10, pady=5)

     boton_insertar_registro = tk.Button(ventana_Administrar_Cultivos, text="Insertar", command=abrir_ventana_insertar_registro)
     boton_insertar_registro.grid(row=2, column=1, padx=10, pady=5)

     boton_modificar_registro = tk.Button(ventana_Administrar_Cultivos, text="Modificar", command=abrir_ventana_modificar_registro)
     boton_modificar_registro.grid(row=3, column=1, padx=10, pady=5)

     boton_eliminar_registro = tk.Button(ventana_Administrar_Cultivos, text="Eliminar", command=abrir_ventana_eliminar_registro)
     boton_eliminar_registro.grid(row=4, column=1, padx=10, pady=5)

     boton_salir = tk.Button(ventana_Administrar_Cultivos, text="Salir", command=ventana_Administrar_Cultivos.quit)
     boton_salir.grid(row=5, column=1, padx=10, pady=10)

def crear_ventana_Administrar_Ganado():
     ventana_Administrar_Cultivos = tk.Tk()
     ventana_Administrar_Cultivos.title("Menú Administrar Ganado-Granja Ucundinamarca")

     etiqueta_leer_registros = tk.Label(ventana_Administrar_Cultivos, text="1.Leer registros de ganado")
     etiqueta_leer_registros.grid(row=1, column=0, padx=30, pady=25)

     etiqueta_insertar_registro = tk.Label(ventana_Administrar_Cultivos, text="2.Insertar registro de ganado")
     etiqueta_insertar_registro.grid(row=2, column=0, padx=30, pady=25)

     etiqueta_modificar_registro = tk.Label(ventana_Administrar_Cultivos, text="3.Modificar registro de ganado")
     etiqueta_modificar_registro.grid(row=3, column=0, padx=30, pady=25)

     etiqueta_eliminar_registro = tk.Label(ventana_Administrar_Cultivos, text="4.Eliminar registro")
     etiqueta_eliminar_registro.grid(row=4, column=0, padx=30, pady=25)

     etiqueta_salir = tk.Label(ventana_Administrar_Cultivos, text="5.Salir")
     etiqueta_salir.grid(row=5, column=0, padx=30, pady=30)

    # Crear botones
     boton_leer_registros = tk.Button(ventana_Administrar_Cultivos, text="Leer", command=leer_registros1)
     boton_leer_registros.grid(row=1, column=1, padx=10, pady=5)

     boton_insertar_registro = tk.Button(ventana_Administrar_Cultivos, text="Insertar", command=abrir_ventana_insertar_registro1)
     boton_insertar_registro.grid(row=2, column=1, padx=10, pady=5)

     boton_modificar_registro = tk.Button(ventana_Administrar_Cultivos, text="Modificar", command=abrir_ventana_modificar_registro1)
     boton_modificar_registro.grid(row=3, column=1, padx=10, pady=5)

     boton_eliminar_registro = tk.Button(ventana_Administrar_Cultivos, text="Eliminar", command=abrir_ventana_eliminar_registro1)
     boton_eliminar_registro.grid(row=4, column=1, padx=10, pady=5)

     boton_salir = tk.Button(ventana_Administrar_Cultivos, text="Salir", command=ventana_Administrar_Cultivos.quit)
     boton_salir.grid(row=5, column=1, padx=10, pady=10)

def crear_ventana_principal():
    # Crear ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal ")

    # Crear etiquetas
    etiqueta_titulo = tk.Label(ventana_principal, text="-Granja Ucundinamarca-", font=("Arial", 23, "bold"))
    etiqueta_titulo.grid(row=0, column=0, columnspan=10, padx=70, pady=30)

    etiqueta_titulo = tk.Label(ventana_principal, text="Administrar cultivos", font=("Arial", 17, "bold"))
    etiqueta_titulo.grid(row=1, column=2, columnspan=10, padx=60, pady=30)

    etiqueta_titulo = tk.Label(ventana_principal, text="Administrar ganado", font=("Arial", 17, "bold"))
    etiqueta_titulo.grid(row=2, column=2, columnspan=10, padx=60, pady=30)

    boton_leer_registros = tk.Button(ventana_principal, text="Cultivos", command=crear_ventana_Administrar_Cultivos)
    boton_leer_registros.grid(row=1, column=1, padx=10, pady=5)

    boton_insertar_registro = tk.Button(ventana_principal, text="Ganado", command=crear_ventana_Administrar_Ganado)
    boton_insertar_registro.grid(row=2, column=1, padx=10, pady=5)

    # Mantener la ventana abierta
    ventana_principal.mainloop()     

crear_ventana_principal()

db.close()