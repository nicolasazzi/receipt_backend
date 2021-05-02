from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Receipt
from .serializers import GetReceiptSerializer, CreateReceiptSerializer

class receipt_list(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        receipts = Receipt.objects.filter(owner=request.user).order_by('-purchase_date')
        serializer = GetReceiptSerializer(receipts, many=True)
        return Response(serializer.data)


class create_receipt(APIView):

    permission_classes = [AllowAny]
    
    def post(self, request):
        receipt = CreateReceiptSerializer(data=request.data)
        print(request.data)
        if receipt.is_valid():
            receipt.save()
            return Response(status=200)
        else:
            return Response(data={'errors': receipt.errors})

class get_statistics(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass
