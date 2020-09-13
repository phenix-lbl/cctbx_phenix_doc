from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index_phenix'),
    path('installation/', views.installation, name='installation_phenix'),
    path('doc_overview/', views.doc_overview, name='doc_overview_phenix'),
    path('examples/', views.examples, name='examples_phenix'),
    path('template/', views.template, name='template_phenix'),
    path('doc_high_level_model_building_intro/', views.doc_high_level_model_building_intro, name='doc_high_level_model_building_intro_phenix'),
    path('doc_model_building_read_files/', views.doc_model_building_read_files, name='doc_model_building_read_files_phenix'),
    path('doc_fit_ligand/', views.doc_fit_ligand, name='doc_fit_ligand_phenix'),
    path('doc_model_building_1/', views.doc_model_building_1, name='doc_model_building_1_phenix'),
    path('doc_model_building_2/', views.doc_model_building_2, name='doc_model_building_2_phenix'),
    path('doc_model_building_segment/', views.doc_model_building_segment, name='doc_model_building_segment_phenix'),
    path('doc_model_building_composite/', views.doc_model_building_composite, name='doc_model_building_composite_phenix'),
]
