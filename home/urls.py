from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mrcaerialSandown/', views.mrcaerialSandown, name='mrcaerialSandown'),
    url(r'^mrcaerialMornington', views.mrcaerialMornington, name='mrcaerialMornington'),
    url(r'^mrcaerialCaulfield/', views.mrcaerialCaulfield, name='mrcaerialCaulfield'),
]
