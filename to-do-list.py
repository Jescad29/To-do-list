import json

# Función para cargar tareas desde el archivo al iniciar


def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# función para guardar tareas en el archivo cada vez que cambian


def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)


# Cargamos las tareas al iniciar el programa
tareas = cargar_tareas()


def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")


def agregar_tarea():
    nombre = input("Escribe la tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    guardar_tareas()
    print("Tarea agregada ✅")


def ver_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas):
            estado = "✔" if tarea["completada"] else "❌"
            print(f"{i+1}. {tarea['nombre']} - {estado}")


def eliminar_tarea():
    ver_tareas()
    try:
        num = int(input("Número de tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            tareas.pop(num-1)
            guardar_tareas()
            print("Tarea eliminada 🗑")
        else:
            print("Número inválido")
    except ValueError:
        print("Por favor ingresa un número válido.")


def marcar_completada():
    ver_tareas()
    try:
        num = int(input("Número de tarea a marcar como completada: "))
        if 1 <= num <= len(tareas):
            tareas[num-1]["completada"] = True
            guardar_tareas()
            print("!Tarea marcada como completada! 🎉")
        else:
            print("Número inválido")
    except ValueError:
        print("Por favor ingresa un número válido.")


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        marcar_completada()
    elif opcion == "5":
        print("¡Hasta luego! 👋")
        break
    else:
        print("Opción inválida")
