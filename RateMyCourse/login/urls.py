from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.login, name = 'login'),
     path('accounts/', include('allauth.urls')),
]
