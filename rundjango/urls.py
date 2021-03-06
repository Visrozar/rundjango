from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf.urls import handler404

handler404 = views.error404

urlpatterns = [
    url(r'^login/$', views.UserFormView.as_view(), name='login'),
    url(r'^logout/$',  views.logout_template, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^mrc/', include('home.urls', namespace='home')),
    url(r'^axe/', include('axe.urls', namespace='axe')),
    url(r'^chief/', include('chief.urls', namespace='chief')),
    url(r'^dell/', include('dell.urls', namespace='dell')),
    url(r'^poll/', include('poll.urls', namespace='poll')),
    url(r'^$', views.index, name='index'),
]
