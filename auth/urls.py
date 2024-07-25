# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/google-login/', views.google_login, name='google_login'),
    # other URLs
]
