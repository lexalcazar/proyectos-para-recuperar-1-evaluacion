# uls app catologo



from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('instrumentos/', views.listado_instrumentos, name='listado_instrumentos'),
    path('instrumentos/nuevo/', views.formulario_instrumento, name='nuevo_instrumento'),
    # ruta para crear una categoria
    path('categorias/nuevo/', views.nuevo_categoria, name='nuevo_categoria'),
    # ruta para crear una marca
    path('marcas/nuevo/', views.nuevo_marca, name='nuevo_marca'),
]
