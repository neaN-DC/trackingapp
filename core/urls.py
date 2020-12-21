from django.urls import path, include
from . import views
from .views import save_player_id
from .views import index


urlpatterns = [
	path('', views.home, name = 'home'),
	path('saveid/', views.save_player_id),
	path('api/', views.index),




]

