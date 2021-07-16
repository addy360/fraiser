from core.views import donate, handleCallback, index
from django.urls import path

urlpatterns = [
    path('<str:username>',index, name="index" ),
    path('donate/<int:profile_id>',donate, name="donate" ),
    path('donate/callback', handleCallback , name='callback')
]