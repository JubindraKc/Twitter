from django.urls import path
from django.conf.urls import url

from bot import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('markovbot/', views.bota, name='bota'),
    # path('botc/', views.botc, name='botc'),
    path('xiaomibot/', views.botb, name='botb'),
    path('', views.home, name='homepage'),



]
