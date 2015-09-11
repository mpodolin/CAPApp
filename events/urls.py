__author__ = 'michaelpodolin'

from django.conf.urls import url
from events import views

urlpatterns = [
    url(r'^calldown/', views.call_down, name='call_downs'),
#    url(r'^profile/', views.profile, name='profile'),
#    url(r'^pt/', views.pt, name='pt'),
]