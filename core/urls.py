from core.views import donate, index
from django.urls import path

urlpatterns = [
    path('',index, name="index" ),
    path('donate',donate, name="donate" ),
]