from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.uno, name='uno'),
    url(r'^$', views.gijonDemografia, name='gijonDemografia'),
    url(r'^santander/$', views.santander, name='santander'),
    url(r'^gijon/gastos/tiempo/$', views.gijonGastosTiempo, name='gijonGastosTiempo'),
    url(r'^gijon/gastos/economico/$', views.gijonGastosEconomico, name='gijonGastosEconomico'),
    url(r'^gijon/gastos/capitulo/$', views.gijonGastosCapitulo, name='gijonGastosCapitulo'),
    url(r'^gijon/gastos/funcional/$', views.gijonGastosFuncional, name='gijonGastosFuncional'),
    url(r'^gijon/gastos/articulo/$', views.gijonGastosArticulo, name='gijonGastosArticulo'),
    url(r'^gijon/gastos/partida/$', views.gijonGastosPartida, name='gijonGastosPartida'),

    url(r'^gijon/demografia/$', views.gijonDemografia, name='gijonDemografia'),

    url(r'^gijon/ingresos/$', views.gijonIngresos, name='gijonIngresos'),

    url(r'^gijon/mapa/$', views.gijonMapa, name='gijonMapa'),

    url(r'^gijon/medioAmbiente/aire/$', views.gijonMedioAmbienteAireGeneral, name='gijonMedioAmbienteAireGeneral'),
    url(r'^gijon/medioAmbiente/aire/SO2/$', views.gijonMedioAmbienteAireSO2, name='gijonMedioAmbienteAireSO2'),
    url(r'^gijon/medioAmbiente/aire/NO/$', views.gijonMedioAmbienteAireNO, name='gijonMedioAmbienteAireNO'),
    url(r'^gijon/medioAmbiente/aire/NO2/$', views.gijonMedioAmbienteAireNO2, name='gijonMedioAmbienteAireNO2'),
    url(r'^gijon/medioAmbiente/aire/CO/$', views.gijonMedioAmbienteAireCO, name='gijonMedioAmbienteAireCO'),
    url(r'^gijon/medioAmbiente/aire/PM10/$', views.gijonMedioAmbienteAirePM10, name='gijonMedioAmbienteAirePM10'),
    url(r'^gijon/medioAmbiente/aire/O3/$', views.gijonMedioAmbienteAireO3, name='gijonMedioAmbienteAireO3'),
    url(r'^gijon/medioAmbiente/aire/TMP/$', views.gijonMedioAmbienteAireTMP, name='gijonMedioAmbienteAireTMP'),
    url(r'^gijon/medioAmbiente/aire/HR/$', views.gijonMedioAmbienteAireHR, name='gijonMedioAmbienteAireHR'),
    url(r'^gijon/medioAmbiente/aire/PRB/$', views.gijonMedioAmbienteAirePRB, name='gijonMedioAmbienteAirePRB'),
    url(r'^gijon/medioAmbiente/aire/RS/$', views.gijonMedioAmbienteAireRS, name='gijonMedioAmbienteAireRS'),
    url(r'^gijon/medioAmbiente/aire/LL/$', views.gijonMedioAmbienteAireLL, name='gijonMedioAmbienteAireLL'),
    url(r'^gijon/medioAmbiente/aire/BEN/$', views.gijonMedioAmbienteAireBEN, name='gijonMedioAmbienteAireBEN'),
    url(r'^gijon/medioAmbiente/aire/TOL/$', views.gijonMedioAmbienteAireTOL, name='gijonMedioAmbienteAireTOL'),
    url(r'^gijon/medioAmbiente/aire/MXIL/$', views.gijonMedioAmbienteAireMXIL, name='gijonMedioAmbienteAireMXIL'),
    url(r'^gijon/medioAmbiente/aire/PM25/$', views.gijonMedioAmbienteAirePM25, name='gijonMedioAmbienteAirePM25'),

    url(r'^gijon/tarjetaCiudadana/$', views.gijonTarjetaCiudadana, name='tarjetaCiudadana'),

    url(r'^gijon/energia/alumbradoPublico/$', views.gijonEnergiaAlumbradoPublico, name='gijonEnergiaAlumbradoPublico'),
]
