from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('destinations',views.destinations,name="destinations"),
]
