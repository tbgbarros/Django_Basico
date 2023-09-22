from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def natal(request):
    data_atual = date.today()
    if data_atual.month == 12 and data_atual.day == 25:
        contexto = {"natal": True}
    else:
        contexto = {"natal": False}
    return render(request, "natal.html", contexto)


def independencia(request):
    data_atual = date.today()
    if data_atual.month == 9 and data_atual.day == 7:
        contexto = {"independencia": True}
    else:
        contexto = {"independencia": False}
    return render(request, "independencia.html", contexto)


def tiradentes(request):
    data_atual = date.today()
    if data_atual.month == 4 and data_atual.day == 21:
        contexto = {"tiradentes": True}
    else:
        contexto = {"tiradentes": False}
    return render(request, "tiradentes.html", contexto)
