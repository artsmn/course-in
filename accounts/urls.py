from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('sign-in/',  views.SignInView.as_view(), name='sign-in'),
    path('sign-up/',  views.SignUpView.as_view(), name='sign-up'),
    path('logout/',  views.LogoutView.as_view(), name='logout'),
]
