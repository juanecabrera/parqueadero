# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from app1.models import Tarifas, Carro, Dueno
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

# Create your views here.
class DuenoListView(ListView):
	model=Dueno

class DuenoDetailView(DetailView):
	model=Dueno

class DuenoUpdateView(UpdateView):
	model=Dueno
	fields='__all__'

class DuenoDeleteView(DeleteView):
	model=Dueno
	success_url=reverse_lazy('dueno_list')


class CarroListView(ListView):
	model=Carro

class CarroDetailView(DetailView):
	model=Carro

class CarroUpdateView(UpdateView):
	model=Carro
	fields='__all__'

class CarroDeleteView(DeleteView):
	model=Carro
	success_url=reverse_lazy('carro_list')

class TarifasListView(ListView):
	model=Tarifas

class TarifasDetailView(DetailView):
	model=Tarifas

class TarifasUpdateView(UpdateView):
	model=Tarifas
	fields='__all__'

class TarifasDeleteView(DeleteView):
	model=Tarifas
	success_url=reverse_lazy('tarifas_list')