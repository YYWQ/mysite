from django.conf.urls import patterns,include,url
from django.contrib import admin
from lists import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', views.login),
    url(r'^$', views.home_page, name="home"),
    url(r'^lists/',include('lists.urls')),

)
