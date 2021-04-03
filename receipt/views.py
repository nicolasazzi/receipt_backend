from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import Receipt
from .serializers import ReceiptSerializer

class receipt_list(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        receipts = Receipt.objects.filter(owner=request.user)
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

