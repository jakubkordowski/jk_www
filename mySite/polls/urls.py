from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.osoba_list.as_view()),
    # path('osoby/', views.osoba_list),
    # path('osoby/<int:pk>/', views.osoba_detail),
    # path('osoby/<str:string>/', views.osoba_string),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
]