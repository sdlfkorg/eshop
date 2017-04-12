from django.conf.urls import url
from members import views 

urlpatterns = [
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^registration/success/$', views.SuccessMessageView.as_view(), name="success")
]
