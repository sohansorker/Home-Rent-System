from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='flats'),
    path('<int:listing_id>', views.flats, name='flat'),
    path('search/', views.search, name='search'),
]

