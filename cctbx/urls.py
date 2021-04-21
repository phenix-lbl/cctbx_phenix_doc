from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('installation/', views.installation, name='installation'),

    path('getting_started/', views.getting_started, name='getting_started'),

    path('documentation_overview/', views.documentation_overview, name='documentation_overview'),

    path('doc_programming_tips/', views.doc_programming_tips, name='doc_programming_tips'),

    path('doc_hklviewer/', views.doc_hklviewer, name='doc_hklviewer'),

    path('doc_hlo_intro/', views.doc_hlo_intro, name='doc_hlo_intro'),
    path('doc_hlo_data_manager/', views.doc_hlo_data_manager, name='doc_hlo_data_manager'),
    path('doc_hlo_model_manager/', views.doc_hlo_model_manager, name='doc_hlo_model_manager'),
    path('doc_hlo_map_manager/', views.doc_hlo_map_manager, name='doc_hlo_map_manager'),
    path('doc_hlo_model_map_manager/', views.doc_hlo_model_map_manager, name='doc_hlo_model_map_manager'),

    path('doc_maps_intro/', views.doc_maps_intro, name='doc_maps_intro'),
    path('doc_maps_boxing/', views.doc_maps_boxing, name='doc_maps_boxing'),

    path('doc_low_flex_array/', views.doc_low_flex_array, name='doc_low_flex_array'),
    path('doc_low_flex_advanced/', views.doc_low_flex_advanced, name='doc_low_flex_advanced'),
    path('doc_phil/', views.doc_phil, name='doc_phil'),

    path('tuto_intro/', views.tuto_intro, name='tuto_intro'),
    path('tuto_hklviewer/', views.tuto_hklviewer, name='tuto_hklviewer'),
    path('tuto_melk_2019/', views.tuto_melk_2019, name='tuto_melk_2019'),
    path('tuto_rigid_body/', views.tuto_rigid_body, name='tuto_rigid_body'),
    path('tuto_cctbx_tour/', views.tuto_cctbx_tour, name='tuto_cctbx_tour'),

    path('script_1/', views.script_1, name='script_1'),
    #
    path('newsletter_artcls/', views.newsletter_artcls, name='newsletter_artcls'),

    path('about/', views.about, name='about'),

    path('test/', views.test, name='test'),
]
