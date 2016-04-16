from django.shortcuts import render


def uno(request):
    return render(request, 'uno.html', {})
def santander(request):
    return render(request, 'santander.html', {})
def gijonGastosTiempo(request):
    return render(request, 'gijonGastosTiempo.html', {})
def gijonGastosEconomico(request):
    return render(request, 'gijonGastosEconomico.html', {})
def gijonGastosCapitulo(request):
    return render(request, 'gijonGastosCapitulo.html', {})
def gijonGastosFuncional(request):
    return render(request, 'gijonGastosFuncional.html', {})
def gijonGastosArticulo(request):
    return render(request, 'gijonGastosArticulo.html', {})
def gijonGastosPartida(request):
    return render(request, 'gijonGastosPartida.html', {})
def gijonIngresos(request):
    return render(request, 'gijonIngresos.html', {})
