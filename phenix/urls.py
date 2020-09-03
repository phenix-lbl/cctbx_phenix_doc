from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index_phenix'),
    path('installation/', views.installation, name='installation_phenix'),
    path('doc_overview/', views.doc_overview, name='doc_overview_phenix'),
    path('examples/', views.examples, name='examples_phenix'),
    path('template/', views.template, name='template_phenix'),
]
