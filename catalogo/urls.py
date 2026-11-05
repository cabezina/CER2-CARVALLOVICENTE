from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/<int:lugar_id>/', views.detalle, name='detalle'),
    path('categoria/<int:categoria_id>/', views.lugares_por_categoria, name='categoria'),
    path('gestion/', views.gestion, name='gestion'),
    path('gestion/agregar/', views.agregar_lugar, name='agregar_lugar'),
    path('gestion/editar/<int:lugar_id>/', views.editar_lugar, name='editar_lugar'),
]
