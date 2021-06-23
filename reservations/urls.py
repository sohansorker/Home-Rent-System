from django.urls import path
from . import views


urlpatterns =[
    path('', views.contact, name='reservation'),
    path('payment/', views.makepayment, name='payment'),
]
