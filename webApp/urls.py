from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^404/$', views.error404, name='error404'),

    url(r'^500/$', views.error500, name='error500'),

    url(r'^inicio/$', views.gijonInicio, name='gijonInicio'),

    # url(r'^$', views.uno, name='uno'),
    url(r'^$', views.gijonInicio, name='gijonInicio'),
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

    url(r'^gijon/sociedad/usoCajeros/$', views.gijonSociedadUsoCajeros, name='gijonSociedadUsoCajeros'),

    url(r'^gijon/economia/presupuestos/gastos/$', views.gijonEconomiaPresupuestosGastos,
        name='gijonEconomiaPresupuestosGastos'),
    url(r'^gijon/economia/presupuestos/ingresos/$', views.gijonEconomiaPresupuestosIngresos,
        name='gijonEconomiaPresupuestosIngresos'),

    url(r'^gijon/elecciones/$', views.gijonElecciones, name='gijonElecciones'),

    url(r'^gijon/empleadosPublicos/antiguedad/$', views.gijonEmpleadosPublicosAntiguedad,
        name='gijonEmpleadosPublicosAntiguedad'),
    url(r'^gijon/empleadosPublicos/sexo/', views.gijonEmpleadosPublicosSexo, name='gijonEmpleadosPublicosSexo'),
    url(r'^gijon/empleadosPublicos/edad/', views.gijonEmpleadosPublicosEdad, name='gijonEmpleadosPublicosEdad'),
    url(r'^gijon/empleadosPublicos/grupoNivel/', views.gijonEmpleadosPublicosGrupoNivel,
        name='gijonEmpleadosPublicosGrupoNivel'),
    url(r'^gijon/empleadosPublicos/regimenJuridico/', views.gijonEmpleadosPublicosRegimenJuridico,
        name='gijonEmpleadosPublicosRegimenJuridico'),
    url(r'^gijon/empleadosPublicos/relacion/', views.gijonEmpleadosPublicosRelacion,
        name='gijonEmpleadosPublicosRelacion'),
    url(r'^gijon/sociedad/reclamacionesSugerencias/', views.gijonReclamacionesSugerencias,
        name='gijonReclamacionesSugerencias'),

    url(r'^gijon/rss/$', views.gijonRSS, name='RSS'),

    url(r'^pruebas/$', views.pruebas, name='pruebas'),

]
