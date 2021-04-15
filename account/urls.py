from django.urls import path


from .views import registration_view, check_phone_view, login_view

app_name = 'account'

urlpatterns = [
    path('register/', registration_view),
    path('login/', login_view),
    path('check/', check_phone_view),
]
