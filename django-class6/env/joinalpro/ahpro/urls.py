from django.urls import path
from . import views

urlpatterns = [
    path('tass/',views.tass),
    path('ai/',views.ai_help)
]