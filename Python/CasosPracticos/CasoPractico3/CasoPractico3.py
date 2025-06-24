import json
agenda_digital = {
    # Primer contacto
    "Daniel Alejandro Sanchez":{
        'nombre': "Daniel Alejandro Sanchez",
        'direccion': "Guayabitos",
        'email' : "daniel@gmail.com",
        'telefono' : "3310101010"
    },
    #Segundo contacto
    "Javier Sanchez Martinez" : {
        'nombre' : "Javier Sanchez Martinez",
        'direccion': "Guadalajara",
        'email' : "javi@gmail.com",
        'telefono' : "3320202020"
    },
    #Tercer contacto
    "Danna Paola Sanchez" : {
        'nombre': "Danna Paola Sanchez",
        'direccion' : "Zapopan",
        'email': "danna@gmail.com",
        'telefono' : "3310111213"
    },
    #Cuarto contacto
    "Karla Ahumada Martinez" : {
        'nombre': "Karla Ahumada Martinez",
        'direccion': "Tonala",
        'email' : "karla@gmail.com",
        'telefono' : "3320201120"
    }
}

def escribir_agenda(nombre_agenda, agenda_digital):
    agenda_fichero = open("agenda_digital", "w")
    agenda_fichero.write(str(agenda_digital))
    agenda_fichero.close()

def leer_agenda(nombre_agenda):
    agenda_digital_lectura = open(nombre_agenda ,"r")
    agenda_digital = agenda_digital_lectura.readlines()
    agenda_digital_lectura.close()
    return eval(agenda_digital[0])

def solicitar_contacto_agenda():
    nombre = input("Ingrese el nombre completo del contacto: ")
    direccion = input("Ingrese la dirección del contacto: ")
    email = input("Ingrese el email del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    contacto = {
        "nombre": nombre,
        "direccion": direccion,
        "email": email,
        "telefono": telefono
    }
    return contacto

def crear_contacto(agenda_digital, nuevo_contacto):
    agenda_digital[nuevo_contacto["nombre"]] = {
        "nombre": nuevo_contacto["nombre"],
        "direccion": nuevo_contacto["direccion"],
        "email": nuevo_contacto["email"],
        "telefono": nuevo_contacto["telefono"]
    }
    return agenda_digital

def consultar_agenda(agenda_digital):
    clave = input("Ingresa el nombre completo del contacto: ")
    print("\n[+]", clave)
    print("\tDirección: ", agenda_digital[clave]["direccion"])
    print("\tEmail: ", agenda_digital[clave]["email"])
    print("\tTelefono: ", agenda_digital[clave]["telefono"])
    return agenda_digital


agenda_digital = leer_agenda(input("Ingrese el nombre del agenda: "))
nuevo_contacto = solicitar_contacto_agenda()
agenda_digital = crear_contacto(agenda_digital, nuevo_contacto)
escribir_agenda("agenda_digital", agenda_digital)
"""
    print(type(agenda_digital[0]))
    print(agenda_digital)
    print("------\n\n" + agenda_digital[0])


agenda1 = leer_agenda("agenda 1", agenda_digital)
"""