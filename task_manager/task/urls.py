from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fahim/', views.fahim, name="Fahim"),
    path('tanvir/', views.tanvir, name="tanvir"),
    path('<str:name>', views.greeting, name="greeting"),
]