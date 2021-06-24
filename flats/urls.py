from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='flats'),
    path('<int:flat_id>', views.flats, name='flat'),
    path('addflats/', views.addflats, name='addflats'),
]

