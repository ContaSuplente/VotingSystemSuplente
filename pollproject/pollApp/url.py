from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'polls'

urlpatterns = [
    path('first', views.index, name='viewIndex'),
    path('<int:question_id>/', views.detail, name='viewDetail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]