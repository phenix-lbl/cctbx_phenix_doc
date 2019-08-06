from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('melk_2019_1', views.melk_2019_1, name='melk_2019_1'),
    path('melk_2019_2', views.melk_2019_2, name='melk_2019_2'),
    path('melk_2019_3', views.melk_2019_3, name='melk_2019_3'),
    path('melk_2019_4', views.melk_2019_4, name='melk_2019_4'),
    path('melk_2019_5', views.melk_2019_5, name='melk_2019_5'),
    path('melk_2019_intro', views.melk_2019_intro, name='melk_2019_intro'),
]
