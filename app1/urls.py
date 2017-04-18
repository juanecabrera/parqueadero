from django.conf.urls import url
from app1 import views

urlpatterns = [
    
    url(r'^dueno/$', views.DuenoListView.as_view(), name='dueno_list'),
    url(r'^dueno/(?P<pk>[0-9]+)/detail/$', views.DuenoDetailView.as_view(), name='dueno_detail'),	
    url(r'^dueno/(?P<pk>[0-9]+)/update/$', views.DuenoUpdateView.as_view(), name='dueno_update'),	
    url(r'^dueno/(?P<pk>[0-9]+)/delete/$', views.DuenoDeleteView.as_view(), name='dueno_delete'),	

    url(r'^carro/$', views.CarroListView.as_view(), name='carro_list'),
    url(r'^carro/(?P<pk>[0-9]+)/detail/$', views.CarroDetailView.as_view(), name='carro_detail'),	
    url(r'^carro/(?P<pk>[0-9]+)/update/$', views.CarroUpdateView.as_view(), name='carro_update'),	
    url(r'^carro/(?P<pk>[0-9]+)/delete/$', views.CarroDeleteView.as_view(), name='carro_delete'),	

    url(r'^tarifas/$', views.TarifasListView.as_view(), name='tarifas_list'),
    url(r'^tarifas/(?P<pk>[0-9]+)/detail/$', views.TarifasDetailView.as_view(), name='tarifas_detail'),	
    url(r'^tarifas/(?P<pk>[0-9]+)/update/$', views.TarifasUpdateView.as_view(), name='tarifas_update'),	
    url(r'^tarifas/(?P<pk>[0-9]+)/delete/$', views.TarifasDeleteView.as_view(), name='tarifas_delete'),	
]