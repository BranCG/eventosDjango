from django.shortcuts import render
from  django.http import  HttpResponse

# Create your views here.

PRODUCTOS = [{'nombre_producto':'TV LED', 'precio' : '109.990'},{'nombre_producto':'LAVADORA', 'precio' : '89.990'},{'nombre_producto':'PC GAMER', 'precio' : '355.990'},{'nombre_producto':'MICRO ONDAS', 'precio' : '20.990'},{'nombre_producto':'SECADORA', 'precio' : '87.990'}]



#Validar que esto es un rut
def validar_rut(rut):
    return (len(rut) == 8 or len(rut) == 9)

COMPRAS = []

def crear_boleta(request):
    while True:
        try:
            while True:
                try:
                    rut = input("Ingrese su rut: ")
                    if not validar_rut(rut):
                        print("RUT NO VALIDO, debe contener 8 o 9 digitos.")
                        return HttpResponse("<h1>ERROR, RUT INVALIDO</h1>", status=400) 
                except ValueError:
                    print("Error, ingrese valores numericos para el RUT.")  
                else:
                    break     

            nombre = input("Ingrese su nombre: ")

            print("Productos disponibles: ")
            for idx,producto in enumerate(PRODUCTOS):
                print(f"{idx + 1}: {producto['nombre_producto']} - ${producto['precio']}")

            producto_idx = int(input("Elige el producto (numero): ")) - 1
            producto_seleccionado = PRODUCTOS[producto_idx]

        except Exception as e:
            print(f"Ha ocurrido un erro{e}")
        
        else:
            print("TU BOLETA ESTA LISTA, ve a la web")
            boleta = {
                "Rut" : rut,
                "Nombre" : nombre,
                "Producto" : producto_seleccionado['nombre_producto'],
                "Precio" : producto_seleccionado['precio'],
            }
            COMPRAS.append(boleta)
            break


    respuesta=f'''
    <html>
    <body>
    <h1>TU BOLETA</h1>
    <p>RUT:{rut}</p>
    <p>NOMBRE:{nombre}</p>
    <p>PRODUCTO: {boleta["Producto"]}</p>
    <p>PRECIO: ${boleta["Precio"]}</p>
    </body>
    </html>  
    '''
    return HttpResponse(respuesta)