# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Dueno(models.Model):
	nombres=models.CharField(max_length=100,blank=True)
	apellidos=models.CharField(max_length=100,blank=True)
	email=models.EmailField(max_length=50)
	telefono=models.CharField(max_length=100,blank=True)
	direccion=models.CharField(max_length=200,blank=True)
	def get_absolute_url(self):
		return reverse('dueno_list')
	def __str__(self):
		return self.nombres+" "+self.apellidos

class Carro(models.Model):
	placa=models.CharField(max_length=100,blank=True)	
	def get_absolute_url(self):
		return reverse('carro_list')
	def __str__(self):
		return self.placa	

class Tarifas(models.Model):
	cliente=models.ForeignKey(Dueno,null=True,blank=True)
	fecha=models.DateField(auto_now_add=False)
	carro=models.ForeignKey(Carro,null=True,blank=True)
	precio=models.CharField(max_length=100,blank=True)
	#def __str__(self):
		#return self.cliente
