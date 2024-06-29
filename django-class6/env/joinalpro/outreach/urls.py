from django.urls import path
from . import views

urlpatterns = [
    path('', views.Link_Building),
    path('keyword-research/', views.Keyword_Research),
    path('content-auditing/', views.Content_Auditing),
    path('ai/', views.Artificial_Inteligence),
]