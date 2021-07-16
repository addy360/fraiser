from core.views import donate, handleCallback, home, index
from django.urls import path

urlpatterns = [
    path('', home, name="home" ),
    path('<str:username>',index, name="index" ),
    path('donate/callback', handleCallback , name='callback'),
    path('donate/<int:profile_id>',donate, name="donate" ),
]