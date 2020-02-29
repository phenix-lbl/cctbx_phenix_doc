from django.conf.urls import url
#from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flex_array', views.flex_array, name='flex_array'),
    url(r'^tutorials', views.tutorials, name='tutorials_intro'),
    url(r'^melk_2019_intro', views.melk_2019_intro, name='melk_2019_intro'),
]
