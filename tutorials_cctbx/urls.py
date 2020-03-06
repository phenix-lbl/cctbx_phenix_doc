from django.conf.urls import url
#from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tutorials', views.tutorials, name='tutorials_intro'),
    url(r'^download', views.download, name='download'),
    url(r'^cctbx_tour', views.cctbx_tour, name='cctbx_tour'),
    url(r'^flex_array', views.flex_array, name='flex_array'),
    url(r'^melk_2019', views.melk_2019, name='melk_2019'),
]
