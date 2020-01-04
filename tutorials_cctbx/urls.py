from django.conf.urls import url
#from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flex_array', views.flex_array, name='flex_array'),
    url(r'^melk_2019_1', views.melk_2019_1, name='melk_2019_1'),
    url(r'^melk_2019_2', views.melk_2019_2, name='melk_2019_2'),
    url(r'^melk_2019_3', views.melk_2019_3, name='melk_2019_3'),
    url(r'^melk_2019_4', views.melk_2019_4, name='melk_2019_4'),
    url(r'^melk_2019_5', views.melk_2019_5, name='melk_2019_5'),
    url(r'^melk_2019_intro', views.melk_2019_intro, name='melk_2019_intro'),
]
