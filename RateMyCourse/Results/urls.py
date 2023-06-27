from django.urls import path
from . import views

urlpatterns = [
    path('results/',views.results, name = 'results'),
    path('logout/', views.logout_view, name='logout'),
]
