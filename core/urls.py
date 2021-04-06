from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import save_player_id


urlpatterns = [
	path('', views.home, name = 'home'),
	path('saveid/', views.save_player_id),

	
]

