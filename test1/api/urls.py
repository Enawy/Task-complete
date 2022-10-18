from django.urls import path
from . import views


urlpatterns = [
    path('', views.getclient),
    path('1/', views.getcar),
    path('2/', views.getcompany),
]
