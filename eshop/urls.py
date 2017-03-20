"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from sausage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.sausage_list, name="home"),
    #url(r'^sausages/(?P<category>.*)$', views.sausage_list, name="sausage_list"),
    url(r'^sausage/$', views.SausageListView.as_view(), name="sausage_list"),
    url(r'^sausage/about/$', views.about, name="about"),
    url(r'^sausage/(?P<pk>\d+)$', views.SausageDetailView.as_view(), name="sausage_detail"),
    url(r'^sausage/(?P<category>.*)$', views.SausageListView.as_view(), name="sausage_list"),


]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
