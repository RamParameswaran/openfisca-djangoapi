from . import plots
from django.shortcuts import render


def BarChart_id(request):
    context = {'plot': plots.varIDBarChart('id')}
    response = render(request, 'plots/barchart.html', context)
    return response


def BarChart_alias(request):
    context = {'plot': plots.varIDBarChart('alias')}
    response = render(request, 'plots/barchart.html', context)
    return response


def Graph(request):
    context = {'plot': plots.graph}
    response = render(request, 'plots/barchart.html', context)
    return response
