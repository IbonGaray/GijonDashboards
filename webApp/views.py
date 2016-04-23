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
