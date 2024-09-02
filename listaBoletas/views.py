from django.shortcuts import render
from boleta.views import COMPRAS
from django.http import HttpResponse

# Create your views here.
def mostrar_boletas(request):
    respuesta = "<html><body><h1>LISTA DE BOLETAS</h1></body></html>"

    for compra in COMPRAS:
        respuesta += f''''
        <p>
        Rut: {compra['Rut']} <br>
        Nombre: {compra['Nombre']} <br>
        Producto: {compra['Producto']} <br>
        Precio: ${compra['Precio']} <br>
        </p>
    '''

    return HttpResponse(respuesta)