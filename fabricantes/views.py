from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Fabricante
from .forms import FabricanteForm


def index(request):
    return render(request, 'fabricantes/index.html', {
        'fabricantes': Fabricante.objects.all()
    })


def view_fabricante(request, id):
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            nuevo_fabricante = Fabricante(
                Fabricante_id=form.cleaned_data['Fabricante_id'],
                Nombre=form.cleaned_data['Nombre'],
                Pais=form.cleaned_data['Pais'],
                sitio_web=form.cleaned_data['sitio_web'],
                logo_url=form.cleaned_data['logo_url'],
                email=form.cleaned_data['email'],
            )
            nuevo_fabricante.save()
            return render(request, 'fabricantes/add.html', {
                'form': FabricanteForm(),
                'success': True
            })
    else:
        form = FabricanteForm()

    return render(request, 'fabricantes/add.html', {
        'form': form
    })


def edit(request, id):
    fabricante = Fabricante.objects.get(pk=id)
    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return render(request, 'fabricantes/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = FabricanteForm(instance=fabricante)

    return render(request, 'fabricantes/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        fabricante = Fabricante.objects.get(pk=id)
        fabricante.delete()
    return HttpResponseRedirect(reverse('index'))
