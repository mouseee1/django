from django.urls import path
from . import views


urlpatterns =[
    path('index',views.index, name='index'),
    path('galeria',views.galeria, name='galeria'),
    path('galeria1',views.galeria1, name='galeria-1'),
    path('artistal',views.artistal, name='artista-l'),
    path('artistai',views.artistai, name='artista-i'),
    path('pinturaslocales',views.pinturaslocales, name='pinturas-locales'),
    path('pi',views.pi, name='p-i'),

]