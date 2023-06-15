from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup',views.signup, name = 'signup'),
     path('',views.login, name = 'login'),
     path('accounts/', include('allauth.urls')),
]
