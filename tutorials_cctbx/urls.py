from django.conf.urls import url
#from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^installation', views.installation, name='installation'),
    url(r'^cctbx_tour', views.cctbx_tour, name='cctbx_tour'),
    url(r'^documentation_overview', views.documentation_overview, name='documentation_overview'),
    url(r'^doc_flex_array', views.doc_flex_array, name='doc_flex_array'),
    url(r'^tutorials', views.tutorials, name='tutorials_intro'),
    url(r'^tuto_melk_2019', views.tuto_melk_2019, name='tuto_melk_2019'),
    url(r'^tuto_rigid_body', views.tuto_rigid_body, name='tuto_rigid_body'),
    url(r'^newsletter_artcls', views.newsletter_artcls, name='newsletter_artcls'),
]
