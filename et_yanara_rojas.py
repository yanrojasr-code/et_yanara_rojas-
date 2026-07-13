# nombre, categoria, talla, color, materia, es_unisex
prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
}

# precio, unidades
bodega = { 
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
    }

def  leer_opcion():
    print(''' ========== MENÚ PRINCIPAL ==========
        1. Unidades por categoría
        2. Búsqueda de prendas por rango de precio
        3. Actualizar precio de prenda
        4. Agregar prenda
        5. Eliminar prenda
        6. Salir
        =====================================
        ''')
    try:
        opcion = int(input("ingrese una opcion: "))
        if 1<= opcion <= 6:
            return opcion
        else:
            print("ingrese un valor entero")
            return False
    except ValueError:
        print("debes seleccionar una opcion valida")

def unidades_categoria(categoria, prendas,bodega):
    print(f"la disponibilidad de {categoria}es:")
    acumulador = 0
    for codigo, datos in prendas.items():
        if datos[1].lower() == categoria.lower():
            acumulador += bodega[codigo][1]
    print(f"el total de {categoria} es: {acumulador} ")

def busqueda_precio(precio_min, precio_max, prendas, bodega):
    lista = []
    for codigo, datos in prendas.items():
        precio, stock = bodega[codigo]
        if precio_min <= precio <= precio_max and stock >0:
            lista.append(f"{datos[1]}--{codigo}")
    if lista:
        lista.sort()
        for prendas in lista:
            print(prendas)
    else:
        print("no hay prendas en ese rango de precio")   
            






while True:
    opcion = leer_opcion()
    if opcion == 1:
        categoria = input("ingrese la categoria a consultar: ")
        unidades_categoria(categoria,prendas,bodega)

    elif opcion ==2:
        try:
            precio_min = int(input("ingrese un precio minimo: "))
            precio_max = int(input("ingrese un precio maximo: "))
            if precio_min <0 or precio_max <0 or precio_min > precio_max:
                print("Debe ingresar valores enteros ")
            else: 
                busqueda_precio(precio_min, precio_max, prendas, bodega)
        except ValueError:
            print("Debe ingresar valores enteros")
