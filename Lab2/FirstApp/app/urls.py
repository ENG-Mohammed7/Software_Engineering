from django.urls import path
from . import views

urlpatterns=[
    path('',views.Hello,name='Hello'),
    path('about',views.about,name='about'),
]