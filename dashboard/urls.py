from django.urls import path

from . import views

urlpatterns =[
    path('user/', views.userdash, name='userdash'),
    path('cancelorder/', views.cancelorder, name='cancelorder'),
    path('homeowner/', views.hodash, name='hodash'),
    path('changestatus/', views.changestatus, name='changestatus'),
    path('editflat/<int:flat_id>', views.editflat, name='editflat'),
    path('vieworder/<int:flat_id>', views.vieworder, name='vieworder'),
    path('editflats/', views.editflats, name='editflats'),
    path('pdfreport/', views.render_pdf_view, name='pdfreport'),
]
