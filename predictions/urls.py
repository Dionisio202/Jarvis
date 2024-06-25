from django.urls import path
from .views import PredictGenre, home

urlpatterns = [
    path('', home, name='home'),
    path('predict/', PredictGenre.as_view(), name='predict-genre'),
]
