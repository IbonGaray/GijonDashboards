from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.uno, name='uno'),
    url(r'^santander/$', views.santander, name='santander'),
    url(r'^gijon/gastos/tiempo/$', views.gijonGastosTiempo, name='gijonGastosTiempo'),
    url(r'^gijon/gastos/economico/$', views.gijonGastosEconomico, name='gijonGastosEconomico'),
    url(r'^gijon/gastos/capitulo/$', views.gijonGastosCapitulo, name='gijonGastosCapitulo'),
    url(r'^gijon/gastos/funcional/$', views.gijonGastosFuncional, name='gijonGastosFuncional'),
    url(r'^gijon/gastos/articulo/$', views.gijonGastosArticulo, name='gijonGastosArticulo'),
    url(r'^gijon/gastos/partida/$', views.gijonGastosPartida, name='gijonGastosPartida'),


    url(r'^gijon/ingresos/$', views.gijonIngresos, name='gijonIngresos'),
]
