from django.urls import path
from . import views

app_name='actualite'

urlpatterns = [
    path('', views.news_index, name='actualite_index'),
    path('article/<slug:slug>/', views.news_detail, name='actualite_detail'),
    path('evenement/<slug:slug>/', views.event_detail, name='actualite_event_detail'),
    
]