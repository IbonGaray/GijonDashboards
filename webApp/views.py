from django.shortcuts import render


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


