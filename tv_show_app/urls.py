from django.urls import path
from . import views

urlpatterns = [
    path('', views.default),
    path('shows/', views.all_shows),
    path('shows/<int:show_id>/', views.show_details),
    path('shows/<int:show_id>/edit/', views.edit_show),
    path('shows/new/', views.enter_show),
    path('shows/create/', views.add_new),
    path('shows/<int:show_id>/destroy/', views.destroy),
    path('shows/<int:show_id>/update', views.update_show),
    
    
]