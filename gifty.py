# -*- coding: utf-8 -*-
# Sistema de Gestión de inventario de Gifty

# Definición clase venta
class Venta:
    def __init__(self, codigo, unidades):
        """
        Constructor para inicializar los atributos de una venta
        codigo: Código único del producto
        unidades: Cantidad de unidades involucradas en la venta
        """
        self.codigo = codigo
        self.unidades = unidades

    def mostrar_informacion(self):
        #Muestra información detallada de la venta.
        return (f"Código: {self.codigo}, Unidades Vendidas: {self.unidades}")

    # Funciones que operan a nivel de Venta (definidas dentro de la clase)
    # -- Funciones para editar venta--

        #def actualizar_codigo
    def actualizar_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo

    #def actualizar_unidades
    def actualizar_unidades (self, nuevo_unidades):
        self.unidades = nuevo_unidades

    # -- Fin Funciones para editar Venta--
    # -- Fin Funciones Clase Venta--

# Lista que contendra las ventas
ventas = []

# Ventas iniciales en programa, no afectan el stock inicial
ventas.append(Venta(1, 25))
ventas.append(Venta(2, 18))
ventas.append(Venta(3, 8))
ventas.append(Venta(4, 9))
ventas.append(Venta(5, 7))
ventas.append(Venta(1, 5))

# --Funciones que operan a nivel de lista Ventas--

def realizar_venta(inventario, ventas):
        while True:
            try:
                codigo = int(input("Ingrese el código del producto: "))
                if verificar_codigo(inventario, codigo):
                    pos_producto = buscar_producto_codigo(inventario, codigo)
                    producto = inventario[pos_producto]
                    print(f"El stock del producto '{producto.nombre}' es: {producto.stock}")
                    break
                else:
                    print("El código no existe. Ingrese un código existente.")
            except ValueError:
                print("Ingrese un código válido (número entero).")

        while True:
            try:
                unidades = int(input("Ingrese cantidad de unidades a vender: "))
                if unidades <= 0:
                    print("La cantidad de unidades a vender debe ser mayor a 0")
                    continue
                break
            except ValueError:
                print("Ingrese una cantidad de unidades a vender válida (número entero).")

        if producto.stock >= unidades:
          producto.actualizar_stock(producto.stock-unidades)
          nueva_venta = Venta(codigo, unidades)
          ventas.append(nueva_venta)
          print(f"Venta exitosa producto - Código: {codigo} - Cantidad de unidades vendidas: {unidades} - Total: ${producto.precio*unidades}.")
        else:
          print(f"Venta fallida producto - Código: {codigo} - Stock insuficiente para vender : {unidades} unidades.")


def producto_mas_vendido(inventario, ventas):

    if not ventas:
        print("No hay ventas registradas.")
        return

    # Crear un diccionario para sumar las unidades vendidas por código de producto
    ventas_por_producto = {}

    for venta in ventas:
        if venta.codigo in ventas_por_producto:
            ventas_por_producto[venta.codigo] = ventas_por_producto[venta.codigo] + venta.unidades
        else:
            ventas_por_producto[venta.codigo] = venta.unidades

    # Ordenar productos
    ventas_ordenadas = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)
    """
    sorted(): función que ordena objetos iterables, por defecto de menor a mayor.
    ventas_por_producto.items(): vista de elementos del diccionario con par (clave,valor), en este caso (codigo,unidades) ej [(1,23),(2,13)] => cod 1, 23 unidades.
    key=lambda x: x[1]: argumento que indica a sorted cómo debe comparar los elementos.
                        La función lambda toma como entrada cada elemento (x), que es un par (codigo, unidades).
                        "x[0]" es el código del producto y "x[1]" son las unidades vendidas.
                        La clave de ordenamiento es "x[1]", es decir, las unidades vendidas.
    reverse=True: argumento que ordena de mayor a menor, coloca en reversa el defecto de la función sorted.
    """

    #Contadores y acumuladores
    contador=1
    total_venta_producto=0
    total_ventas=0

    # Buscar el producto correspondiente en el inventario
    print("\nProductos más vendidos (de mayor a menor):")
    for codigo, unidades in ventas_ordenadas:
      for producto in inventario:
          if producto.codigo == codigo:
              print(f"\nProducto nro: {contador}")
              print(f"Nombre: {producto.nombre}")
              print(f"Unidades Totales Vendidas: {unidades}")
              total_venta_producto = unidades*producto.precio
              print(f"Total vendido: {total_venta_producto}")
              total_ventas=total_ventas+total_venta_producto
              contador=contador+1
    print(f"\nTotal de ventas: {total_ventas}")

# Definición de clase producto
class Producto:
    def __init__(self, nombre, precio, stock, codigo, umbral):
        """
        Constructor para inicializar los atributos de un producto
        nombre: Nombre del producto
        precio: Precio del producto
        stock: Cantidad disponible en inventario
        codigo: Código único del producto
        umbral: Nivel de stock bajo el cual se activa una alerta
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.codigo = codigo
        self.umbral = umbral

    def mostrar_informacion(self):
        #Muestra información detallada del producto.
        return (f"Producto: {self.nombre}, Precio: ${self.precio}, "
                f"Stock: {self.stock}, Código: {self.codigo}, "
                f"Umbral: {self.umbral}")

    # Funciones que operan a nivel de Producto (definidas dentro de la clase)

    # Método para actualizar el precio
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    #def actualizar_nombre
    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    #def actualizar_stock
    def actualizar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    #def actualizar_codigo
    def actualizar_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo

    #def actualizar_umbral
    def actualizar_umbral (self, nuevo_umbral):
        self.umbral = nuevo_umbral

    # -- Fin Funciones Clase producto--

# Lista que contendra los Productos en catálogo, haciendo de inventario
inventario = []

# Inventario base de Gifty
inventario.append(Producto("Taza personalizable", 3500, 50, 1, 10))
inventario.append(Producto("Cuaderno Personalizable 100 Hojas", 2500, 30, codigo=2, umbral=5))
inventario.append(Producto("Lapiz Corazón", 1000, 100, codigo=3, umbral=20))
inventario.append(Producto("Llavero Perrito", 1200, 15, codigo=4, umbral=16))
inventario.append(Producto("Caja de regalo", 2000, 25, codigo=5, umbral=10))

# --Funciones que operan a nivel de lista--

#def verificar_codigo (Un codigo no puede estar repetido, utilizado en agregar_producto y editar_producto)
def verificar_codigo(inventario, codigo):
          """Verifica si un código ya existe en el inventario."""
          for producto in inventario:
              if producto.codigo == codigo:
                  return True  # El código ya existe
          return False  # El código no existe

def buscar_producto_nombre(inventario, nombre):
  #devuelve la posicion en la lista del producto por su nombre
  for i, producto in enumerate(inventario):
    if producto.nombre == nombre:
       return i
  return -1  # Retorna -1 si no encuentra el producto

def buscar_producto_codigo(inventario, codigo):
  #devuelve la posicion en la lista del producto por su codigo
  for i, producto in enumerate(inventario):
    if producto.codigo == codigo:
      return i
  return -1  # Retorna -1 si no encuentra el producto


def buscar_producto(inventario, accion):
    #Integración de las funciones buscar_producto_nombre y buscar_producto_codigo
    #preguntar en menu si desea buscar por nombre o por codigo
    while True:
        print(f"\n¿Cómo desea buscar el producto a {accion}?")
        print("1. Por nombre")
        print("2. Por código")
        print("3. Volver al menú principal")

        try:
            opcion_busqueda = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion_busqueda == 1:
            nombre_producto = input(f"Ingrese el nombre del producto a {accion}: ")
            indice = buscar_producto_nombre(inventario, nombre_producto)
            if indice != -1:
                return indice
            else:
                print("Producto no encontrado.")
                continue
        elif opcion_busqueda == 2:
            try:
                codigo_producto = int(input(f"Ingrese el código del producto a {accion}: "))
                indice = buscar_producto_codigo(inventario, codigo_producto)
                if indice != -1:
                    return indice
                else:
                    print("Producto no encontrado.")
                    continue
            except ValueError:
                print("Por favor, ingrese un código válido (número entero).")
                continue
        elif opcion_busqueda == 3:
            return -1  # Regresa al menú principal
        else:
            print("Opción inválida. Por favor, seleccione 1, 2 o 3.")


#def agregar_producto
    #pedir datos para agregar a inventario (.append)
    #usar verificar_codigo
def agregar_producto(inventario):
        # Se solicita el nombre al principio de acuerdo al orden de los productos ya existentes
        nombre = input("Ingrese el nombre del producto: ")

        while True:
            try:
                precio = int(input("Ingrese el precio del producto: "))
                if precio <=0:
                    print("El precio debe ser mayor que cero.")
                    continue
                break
            except ValueError:
                print("Ingrese un precio válido (número).")

        while True:
            try:
                stock = int(input("Ingrese el stock inicial del producto: "))
                if stock < 0:
                    print("El stock no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Ingrese un stock válido (número entero).")

        while True:
            try:
                codigo = int(input("Ingrese el código del producto: "))
                if verificar_codigo(inventario, codigo):
                    print("El código ya existe. Ingrese un código único.")
                else:
                    break
            except ValueError:
                print("Ingrese un código válido (número entero).")

        while True:
            try:
                umbral = int(input("Ingrese el umbral de stock mínimo: "))
                if umbral < 0:
                    print("El umbral no puede ser negativo")
                    continue
                break
            except ValueError:
                print("Ingrese un umbral válido (número entero).")

        nuevo_producto = Producto(nombre, precio, stock, codigo, umbral)
        inventario.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado exitosamente al inventario.")


def eliminar_producto(inventario):
    indice = buscar_producto(inventario, "eliminar")
    if indice == -1:
        print("Regresando al menú principal...")
        return

    producto = inventario[indice]
    print("\nProducto encontrado:")
    print(producto.mostrar_informacion())

    while True:
        confirmacion = input("\n¿Está seguro de que desea eliminar este producto? (s/n): ").lower()
        if confirmacion == 's':
            inventario.pop(indice)
            print(f"Producto '{producto.nombre}' eliminado exitosamente.")
            return
        elif confirmacion == 'n':
            print("Eliminación cancelada.")
            return
        else:
            print("Opción inválida. Por favor, ingrese 's' o 'n'.")

def editar_producto():

  indice = buscar_producto(inventario, "editar")
  if indice == -1:
    print("Regresando al menú principal...")
    return

  producto = inventario[indice]
  print("\nProducto encontrado:")
  while True:
    print("\nMenú Edición Producto")
    print(producto.mostrar_informacion())
    print("\n¿Qué desea editar?")
    print("1. Nombre")
    print("2. Precio")
    print("3. Stock")
    print("4. Código")
    print("5. Umbral")
    print("6. Volver al Menú Principal")

    try:
      opcion_edicion = int(input("Seleccione una opción: "))
    except ValueError:
      print("Por favor, ingrese un número válido.")
      continue

    if opcion_edicion == 1:
      nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
      producto.actualizar_nombre(nuevo_nombre)
      print(f"Nombre del producto actualizado a '{nuevo_nombre}'.")

    elif opcion_edicion == 2:
      try:
        nuevo_precio = int(input("Ingrese el nuevo precio del producto: "))
        if nuevo_precio > 0:
          producto.actualizar_precio(nuevo_precio)
          print(f"Precio del producto actualizado a ${nuevo_precio}.")
        else:
          print("El precio debe ser mayor que cero.")
      except ValueError:
        print("Por favor, ingrese un precio válido.")

    elif opcion_edicion == 3:
      try:
        nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
        if nuevo_stock >= 0:
          producto.actualizar_stock(nuevo_stock)
          print(f"Stock del producto actualizado a {nuevo_stock}.")
        else:
          print("El stock no puede ser negativo.")
      except ValueError:
        print("Por favor, ingrese un stock válido.")

    elif opcion_edicion == 4:
      while True:
        try:
          nuevo_codigo = int(input("Ingrese el nuevo código del producto: "))
          if not verificar_codigo(inventario, nuevo_codigo):
            producto.actualizar_codigo(nuevo_codigo)
            print(f"Código del producto actualizado a {nuevo_codigo}.")
            break
          else:
            print("El código ya existe. Ingrese un código único.")
        except ValueError:
          print("Por favor, ingrese un código válido.")

    elif opcion_edicion == 5:
      try:
        nuevo_umbral = int(input("Ingrese el nuevo umbral de stock mínimo: "))
        if nuevo_umbral >= 0:
          producto.actualizar_umbral(nuevo_umbral)
          print(f"Umbral de stock actualizado a {nuevo_umbral} unidades.")
        else:
          print("El umbral no puede ser negativo.")
      except ValueError:
        print("Ingrese un umbral válido.")

    elif opcion_edicion == 6:
      print("Regresando al menú principal...")
      return
    else:
      print("Por favor, seleccione una opción válida (1-6).")
      continue


def mostrar_inventario(inventario_tienda):
    # Mostrar información de cada producto en el inventario
    contador_productos = 1
    for producto in inventario_tienda:
        print(f"Producto {contador_productos}:")
        print(producto.mostrar_informacion())
        contador_productos += 1  # Incrementar el contador

import pandas as pd
import os
from datetime import datetime

def fecha_hora_actual():
    #Fecha y hora en format
    fecha_actual = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    return fecha_actual

def inventario_lista_a_df(inventario_tienda):
    datos_inventario = [
        {
            "Nombre": producto.nombre,
            "Precio": producto.precio,
            "Stock": producto.stock,
            "Código": producto.codigo,
            "Umbral": producto.umbral
        }
        for producto in inventario_tienda
    ]

    #DataFrame de pandas
    df = pd.DataFrame(datos_inventario)
    return df

def exportar_inventario_xlsx(inventario_tienda):

    df=inventario_lista_a_df(inventario_tienda)

    #Fecha y hora en format
    fecha_actual = fecha_hora_actual()

    #Crear carpeta "Reporteria_Gifty_xlsx" si no existe
    carpeta = "Reporteria_Gifty_xlsx"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Ruta completa para guardar el archivo
    nombre_archivo = os.path.join(carpeta, f"inventario_gifty_{fecha_actual}.xlsx")

    df.to_excel(nombre_archivo, index=False)

    print(f"Archivo '{nombre_archivo}' creado con éxito.")

def exportar_inventario_json(inventario_tienda):

    df=inventario_lista_a_df(inventario_tienda)

    #Fecha y hora en format
    fecha_actual = fecha_hora_actual()

    #Crear carpeta "Reporteria_Gifty_json" si no existe
    carpeta = "Reporteria_Gifty_json"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Ruta completa para guardar el archivo
    nombre_archivo = os.path.join(carpeta, f"inventario_gifty_{fecha_actual}.json")

    df.to_json(nombre_archivo, orient='records', force_ascii=False, index=False)

    print(f"Archivo '{nombre_archivo}' creado con éxito.")


def menu_reporteria():
    ancho = 60

    while True:
        print("\n"+"=== Reportería Gifty ===".center(ancho))
        print("1. Exportar Inventario xlsx".center(ancho))
        print("2. Exportar Inventario json".center(ancho))
        print("3. Productos bajo Stock".center(ancho))
        print("4. Producto vendidos (mayor a menor)".center(ancho))
        print("5. Salir".center(ancho))

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
            continue

        if opcion == 1:
            print("\nInventario Gifty a Excel.")
            exportar_inventario_xlsx(inventario)
            return
        elif opcion == 2:
            print("\nInventario Gifty a Json.")
            exportar_inventario_json(inventario)
        elif opcion == 3:
            print("\nProductos con bajo Stock.")
            producto_bajo_stock(inventario)
        elif opcion == 4:
            print("\nProducto más vendido.")
            producto_mas_vendido(inventario, ventas)
        elif opcion == 5:
            print("\nSaliendo del gestor de Reportería Gifty.")
            break
        else:
            print("\nPor favor, seleccione una opción válida (1-5).")


def producto_bajo_stock(inventario_tienda):
    hay_stock_bajo = False
    for producto in inventario_tienda:
        if producto.stock < producto.umbral:
            print(f"Producto '{producto.nombre}' Cod:{producto.codigo}. Stock actual: {producto.stock}. Mínimo Sugerido: {producto.umbral}")
            hay_stock_bajo = True
    if not hay_stock_bajo:
        print("Todos los productos cuentan con stock.")

def notificacion_stock(inventario_tienda):
  notificacion = False
  for producto in inventario_tienda:
    if producto.stock < producto.umbral:
        notificacion = True
  if notificacion == True:
    print("\n*** Alerta: Hay productos bajos en Stock ***")
  return

#Función menu_gifty, la cual hará de eje y referenciará a las demás funciones en sus opciones.
def menu_gifty():
    # Definir ancho máximo del menú, para posterior centrado
    ancho = 60
    # Para mejorar legibilidad, las interacciones no se centrarán

    # Imprimir las líneas ajustadas al mismo ancho

    #print("\n": Comando que genera salto de linea en un texto
    #.center(ancho): centra un texto respecto a un valor numérico (cantidad de caracteres), en este caso almacenado en 'ancho'


    while True:
        notificacion_stock(inventario)

        print("\n=== Bienvenido al Sistema de Venta y gestión de Inventario Gifty ===".center(ancho))
        print("================= Con Gifty todo momento es Pretty =================".center(ancho))
        print("\n====================================================================".center(ancho))
        print(""+"===================== Menú de Opciones =============================".center(ancho))
        print("1. Realizar venta     ".center(ancho))
        print("2. Mostrar inventario ".center(ancho))
        print("3. Agregar producto   ".center(ancho))
        print("4. Editar producto    ".center(ancho))
        print("5. Eliminar producto  ".center(ancho))
        print("6. Reportería         ".center(ancho))
        print("7. Salir              ".center(ancho))
        print("====================================================================\n".center(ancho))
        # Opcion buscar producto en especifico

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
            continue
        if opcion == 1:
            print("\nVenta Producto")
            realizar_venta(inventario, ventas)
        elif opcion == 2:
            print("\nInventario Gifty.")
            mostrar_inventario(inventario)
        elif opcion == 3:
            print("\nAgregar producto")
            agregar_producto(inventario)
        elif opcion == 4:
            print("\nEditar producto")
            editar_producto()
        elif opcion == 5:
            print("\nEliminar producto")
            eliminar_producto(inventario)
        elif opcion == 6:
            print("\nReportería Gifty")
            menu_reporteria()
        elif opcion == 7:
            print("\nSaliendo del gestor de inventario Gifty. ¡Hasta luego!")
            break
        else:
            print("\nPor favor, seleccione una opción válida (1-7).")


# Llamar a la función para mostrar el menú
menu_gifty()