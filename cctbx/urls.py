from django.conf.urls import url
from django.urls import include, path

from . import views

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^about', views.about, name='about'),
#    url(r'^installation', views.installation, name='installation'),
#    url(r'^cctbx_tour', views.cctbx_tour, name='cctbx_tour'),
#    #
#    url(r'^documentation_overview', views.documentation_overview, name='documentation_overview'),
#    url(r'^doc_flex_array', views.doc_flex_array, name='doc_flex_array'),
#    url(r'^doc_phil', views.doc_phil, name='doc_phil'),
#    url(r'^doc_high_level_objects', views.doc_high_level_objects, name='doc_high_level_objects'),
#    url(r'^doc_data_manager', views.doc_data_manager, name='doc_data_manager'),
#    url(r'^doc_model_manager', views.doc_model_manager, name='doc_model_manager'),
#    url(r'^doc_map_manager', views.doc_map_manager, name='doc_map_manager'),
#    url(r'^doc_model_map_manager', views.doc_model_map_manager, name='doc_model_map_manager'),
#    #
#    url(r'^getting_started', views.getting_started, name='getting_started'),
#    #
#    url(r'^tutorials', views.tutorials, name='tutorials_intro'),
#    url(r'^tuto_melk_2019', views.tuto_melk_2019, name='tuto_melk_2019'),
#    url(r'^tuto_rigid_body', views.tuto_rigid_body, name='tuto_rigid_body'),
#    #
#    url(r'^newsletter_artcls', views.newsletter_artcls, name='newsletter_artcls'),
#    url(r'^test', views.test, name='test'),
#]

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('installation/', views.installation, name='installation'),
    path('cctbx_tour/', views.cctbx_tour, name='cctbx_tour'),
    #
    path('documentation_overview/', views.documentation_overview, name='documentation_overview'),
    path('doc_flex_array/', views.doc_flex_array, name='doc_flex_array'),
    path('doc_phil/', views.doc_phil, name='doc_phil'),
    path('doc_high_level_objects/', views.doc_high_level_objects, name='doc_high_level_objects'),
    path('doc_data_manager/', views.doc_data_manager, name='doc_data_manager'),
    path('doc_model_manager/', views.doc_model_manager, name='doc_model_manager'),
    path('doc_map_manager/', views.doc_map_manager, name='doc_map_manager'),
    path('doc_model_map_manager/', views.doc_model_map_manager, name='doc_model_map_manager'),
    #
    path('getting_started/', views.getting_started, name='getting_started'),
    #
    path('tutorials/', views.tutorials, name='tutorials_intro'),
    path('tuto_melk_2019/', views.tuto_melk_2019, name='tuto_melk_2019'),
    path('tuto_rigid_body/', views.tuto_rigid_body, name='tuto_rigid_body'),
    #
    path('newsletter_artcls/', views.newsletter_artcls, name='newsletter_artcls'),
    path('test/', views.test, name='test'),
]
