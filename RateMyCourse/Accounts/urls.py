from django.urls import path
from . import views


app_name = 'Accounts'

urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('login/', views.login, name='login'),
    path('results/logout/', views.logout_view, name='logout'),
]
