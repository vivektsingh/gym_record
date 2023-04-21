from . import views
from django.urls import path




urlpatterns = [
    path('', views.Home, name='home'),
    path('add_member/', views.add_member, name='add_member'),
    path('members/', views.members, name='members'),
    

    
]