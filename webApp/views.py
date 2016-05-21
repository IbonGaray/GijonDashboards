from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def error404(request):
    return render(request, '404.html', {})
def error500(request):
    return render(request, '500.html', {})

def uno(request):
    return render(request, 'uno.html', {})
def santander(request):
    return render(request, 'santander.html', {})

def gijonGastosTiempo(request):
    return render(request, 'gastos/gijonGastosTiempo.html', {})
def gijonGastosEconomico(request):
    return render(request, 'gastos/gijonGastosEconomico.html', {})
def gijonGastosCapitulo(request):
    return render(request, 'gastos/gijonGastosCapitulo.html', {})
def gijonGastosFuncional(request):
    return render(request, 'gastos/gijonGastosFuncional.html', {})
def gijonGastosArticulo(request):
    return render(request, 'gastos/gijonGastosArticulo.html', {})
def gijonGastosPartida(request):
    return render(request, 'gastos/gijonGastosPartida.html', {})

def gijonIngresos(request):
    return render(request, 'ingresos/gijonIngresos.html', {})

def gijonMapa(request):
    return render(request, 'mapas/gijonMapa.html', {})

def gijonDemografia(request):
    return render(request, 'demografia/gijonDemografiaGeneral.html', {})

def gijonMedioAmbienteAireGeneral(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireGeneral.html', {})
def gijonMedioAmbienteAireSO2(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireSO2.html', {})
def gijonMedioAmbienteAireNO(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireNO.html', {})
def gijonMedioAmbienteAireNO2(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireNO2.html', {})
def gijonMedioAmbienteAireCO(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireCO.html', {})
def gijonMedioAmbienteAirePM10(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAirePM10.html', {})
def gijonMedioAmbienteAireO3(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireO3.html', {})
def gijonMedioAmbienteAireTMP(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireTMP.html', {})
def gijonMedioAmbienteAireHR(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireHR.html', {})
def gijonMedioAmbienteAirePRB(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAirePRB.html', {})
def gijonMedioAmbienteAireRS(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireRS.html', {})
def gijonMedioAmbienteAireLL(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireLL.html', {})
def gijonMedioAmbienteAireBEN(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireBEN.html', {})
def gijonMedioAmbienteAireTOL(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireTOL.html', {})
def gijonMedioAmbienteAireMXIL(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAireMXIL.html', {})
def gijonMedioAmbienteAirePM25(request):
    return render(request, 'medioAmbiente/gijonMedioAmbienteAirePM25.html', {})

def gijonTarjetaCiudadana(request):
    return render(request, 'tarjetaCiudadana/gijonTarjetaCiudadana.html', {})

def gijonEnergiaAlumbradoPublico(request):
    return render(request, 'energia/gijonEnergiaAlumbradoPublico.html', {})

def gijonSociedadUsoCajeros(request):
    return render(request, 'sociedad/gijonSociedadUsoCajeros.html', {})

def gijonEconomiaPresupuestosGastos(request):
    return render(request, 'economia/gijonEconomiaPresupuestosGastos.html', {})
def gijonEconomiaPresupuestosIngresos(request):
    return render(request, 'economia/gijonEconomiaPresupuestosIngresos.html', {})

def gijonElecciones(request):
    return render(request, 'sectorPublico/gijonElecciones.html', {})

def gijonEmpleadosPublicosAntiguedad(request):
    return render(request, 'sectorPublico/gijonEmpleadosPublicosAntiguedad.html', {})
def gijonEmpleadosPublicosSexo(request):
    return render(request, 'sectorPublico/gijonEmpleadosPublicosSexo.html', {})
def gijonEmpleadosPublicosEdad(request):
    return render(request, 'sectorPublico/gijonEmpleadosPublicosEdad.html', {})
def gijonEmpleadosPublicosGrupoNivel(request):
    return render(request, 'sectorPublico/gijonEmpleadosPublicosGrupoNivel.html', {})
def gijonEmpleadosPublicosRegimenJuridico(request):
    return render(request, 'sectorPublico/gijonEmpleadosPublicosRegimenJuridico.html', {})
def gijonEmpleadosPublicosRelacion(request):
    return render(request, 'sectorPublico/gijonEmpleadosPublicosRelacion.html', {})

#Gestion usuarios
def pruebas(request):
     return render(request, 'usuarios/nuevoUsuario.html', {})

