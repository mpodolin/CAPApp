__author__ = 'michaelpodolin'

from django.conf.urls import url
from promotions import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^pt/', views.pt, name='pt'),
]