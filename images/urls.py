from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.home, name='home'),
    path('image/<int:image_id>/', views.image_detail, name='image_detail'),
    path('search/', views.search, name='search'),
]