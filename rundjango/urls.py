from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/$', views.UserFormView.as_view(), name='login'),
    url(r'^logout/$',  views.logout_template, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^mrc/', include('home.urls', namespace='home')),
    url(r'^$', views.index, name='index'),
]
