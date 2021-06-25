from django.urls import path

from . import views

urlpatterns =[
    path('user/', views.userdash, name='userdash'),
    path('homeowner/', views.hodash, name='hodash'),
    path('pdfreport/', views.render_pdf_view, name='pdfreport'),
]
