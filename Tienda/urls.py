from django.urls import path
from .views import mostrarInicio,mostrarFormulario, mostrarVideo, mostrarPokeApi, listarProductos, \
                    crearProductos, eliminarProductos, modificarProductos, registrar, agregar_producto, \
                    limpiar_carrito, restar_producto, eliminar_producto, generarBoleta

urlpatterns=[ 
    path('', mostrarInicio, name="inicio"),
    path('formulario/', mostrarFormulario, name="formulario"),
    path('video.html/', mostrarVideo, name="video"),
    path('pokeapi.html/', mostrarPokeApi, name="pokeapi"),
    path('listarproductos/', listarProductos, name="listarProductos"),
    path('crearproductos/', crearProductos, name="crearProductos"),
    path('eliminarProductos/<id>', eliminarProductos, name="eliminarProductos"),
    path('modificarproductos/<id>', modificarProductos, name="modificarProductos"),
    path('registrar/', registrar, name="registrar"),

    path('agregar_producto/<id>', agregar_producto, name="agregar"),
    path('eliminar_producto/<id>', eliminar_producto, name="eliminar"),
    path('restar_producto/<id>', restar_producto, name="restar"),
    path('limpiar_carrito', limpiar_carrito, name="limpiar"),
    path('generarBoleta/', generarBoleta, name="generarBoleta"),
]