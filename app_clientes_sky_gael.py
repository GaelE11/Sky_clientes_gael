import os
import json

# Definir carpeta donde se almacenarán los clientes
CLIENTES_DIR = "clientes"

# Si la carpeta no existe, crearla
if not os.path.exists(CLIENTES_DIR):
    os.makedirs(CLIENTES_DIR)

def crear_cliente(nombre, servicio):

    archivo = f"{CLIENTES_DIR}/{nombre}.json"
    
    if os.path.exists(archivo):  # Si el cliente ya existe, agregar el nuevo servicio
        with open(archivo, "r+") as f:
            data = json.load(f)
            data["servicios"].append(servicio)
            f.seek(0)
            json.dump(data, f, indent=4)
    else:  # Si el cliente no existe, crear un nuevo archivo
        cliente = {"nombre": nombre, "servicios": [servicio]}
        with open(archivo, "w") as f:
            json.dump(cliente, f, indent=4)
    
    print(f"Cliente {nombre} actualizado con el servicio {servicio}")

def consultar_cliente(nombre):

    archivo = f"{CLIENTES_DIR}/{nombre}.json"
    
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            cliente = json.load(f)
            return cliente
    else:
        return None

def listar_clientes():
 
    return [f.split(".")[0] for f in os.listdir(CLIENTES_DIR) if f.endswith(".json")]

# Menú interactivo en la terminal
if __name__ == "__main__":
    while True:
        print("\n1. Agregar Cliente")
        print("2. Consultar Cliente")
        print("3. Listar Clientes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            servicio = input("Servicio contratado (telefonía, internet, TV de paga): ")
            crear_cliente(nombre, servicio)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente: ")
            cliente = consultar_cliente(nombre)
            print(cliente if cliente else "Cliente no encontrado.")
        elif opcion == "3":
            print("Clientes registrados:", listar_clientes())
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
