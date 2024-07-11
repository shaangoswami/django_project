from django.urls import path
from . import views

urlpatterns = {
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
    path('analyze/', views.analyze, name='analyze'),
   
}