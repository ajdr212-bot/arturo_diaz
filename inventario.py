
# Sistema de gestion de inventario
# Asignatura: Procesos Informaticos

inventario = {
    "Teclado": 10,
    "Mouse": 15,
    "Monitor": 5
}

def mostrar_inventario():
    print("=== INVENTARIO DE PRODUCTOS ===")

    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")

def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad

agregar_producto("Notebook", 3)
mostrar_inventario()
