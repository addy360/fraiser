from core.views import donate, handleCallback, index
from django.urls import path

urlpatterns = [
    path('',index, name="index" ),
    path('donate',donate, name="donate" ),
    path('donate/callback', handleCallback , name='callback')
]