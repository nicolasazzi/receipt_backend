
from django.urls import path
from .views import receipt_list, create_receipt

urlpatterns = [
    path('all/', receipt_list.as_view()),
    path('create/', create_receipt.as_view())
]
