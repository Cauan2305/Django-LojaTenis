from django.contrib import admin
from django.urls import path,include
from .views import IndexView,CollectionView,RacingView,ShoesView,ContatoView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('coleção/',CollectionView.as_view(),name='coleção'),
    path('bota/',RacingView.as_view(),name='bota'),
    path('tenis/',ShoesView.as_view(),name='tenis'),
    path('contato/',ContatoView.as_view(),name='contato'),

]