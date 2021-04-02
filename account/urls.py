from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import registration_view, check_phone_view

app_name = 'account'

urlpatterns = [
    path('register/', registration_view),
    path('login/', obtain_auth_token),
    path('check/', check_phone_view),
]
