from django.urls import path
from .views import youtube

urlpatterns = [
    path('', youtube, name='youtube'),
]
