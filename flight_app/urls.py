from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_route, name='add_route'),
    path('view/', views.view_routes, name='view_routes'),
    path('nth/', views.nth_node, name='nth_node'),
    path('longest/', views.longest_route, name='longest_route'),
    path('shortest/', views.shortest_route, name='shortest_route'),
    path('', views.home, name='home'),  # This is the root URL

]
