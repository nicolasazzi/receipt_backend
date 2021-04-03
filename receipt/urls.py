
from django.urls import path
from .views import receipt_list

urlpatterns = [
    path('all/', receipt_list.as_view()),
]
