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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from sausage import views
from members.forms import LoginForm

# from django.contrib.auth.forms import AdminPasswordChangeForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.sausage_list, name="home"),
    #url(r'^sausages/(?P<category>.*)$', views.sausage_list, name="sausage_list"),
    url(r'^sausage/$', views.SausageListView.as_view(), name="sausage_list"),
    url(r'^sausage/create$', views.SausageCreateView.as_view(), name="sausage_create"),
    url(r'^sausage/update/(?P<pk>\d+)$', views.SausageUpdateView.as_view(), name="sausage_update"),
    url(r'^sausage/delete/(?P<pk>\d+)$', views.SausageDeleteView.as_view(), name="sausage_delete"),
    url(r'^sausage/about$', views.AboutView.as_view(), name="about"),

    url(r'^sausage/(?P<pk>\d+)$', views.SausageDetailView.as_view(), name="sausage_detail"),
    url(r'^sausage/(?P<category>.*)$', views.SausageListView.as_view(), name="sausage_list"),
    


    url(r'^login/$', auth_views.login, {'template_name': 'members/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'sausage_list'}, name='logout'),
    url(r'^password_change/$', 
        auth_views.password_change, 
        {
        'post_change_redirect' : 'about',
        'template_name': 'members/password_change.html', 
        'password_change_form': PasswordChangeForm},
         name='password_change'),
    url(r'^password_change_done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^socialauth/', include('social_django.urls', namespace='social')),


    ]
    

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
