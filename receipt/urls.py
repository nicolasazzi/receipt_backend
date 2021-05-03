
from django.urls import path
from .views import receipt_list, create_receipt, get_statistics

urlpatterns = [
    path('all/', receipt_list.as_view()),
    path('create/', create_receipt.as_view()),
    path('stats/', get_statistics.as_view())
]
