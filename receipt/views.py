from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Avg, Count, FloatField

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Receipt
from .serializers import GetReceiptSerializer, CreateReceiptSerializer

from datetime import datetime

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
        if receipt.is_valid():
            receipt.save()
            return Response(status=200)
        else:
            return Response(data={'errors': receipt.errors})

class get_statistics(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        all_receipts = Receipt.objects.filter(owner=request.user)

        this_month_sum = all_receipts.filter(
            purchase_date__year=datetime.now().year, 
            purchase_date__month=datetime.now().month,
            ).aggregate(Sum('total'))

        this_year_sum = all_receipts.filter(
            purchase_date__year=datetime.now().year,
            ).aggregate(Sum('total'))

        total_each_month = all_receipts.values('purchase_date__year', 'purchase_date__month').annotate(Sum('total'))
        total_all_months = 0

        for value in total_each_month:
            total_all_months += value['total__sum']
            
        average_monthly = total_all_months / len(total_each_month)

        total_each_year = all_receipts.values('purchase_date__year').annotate(Sum('total'))
        total_all_years = 0

        for value in total_each_year:
            total_all_years += value['total__sum']

        average_yearly = total_all_years / len(total_each_year)

        data = {
            'this_month_sum': this_month_sum['total__sum'],
            'this_year_sum': this_year_sum['total__sum'],
            'average_yearly': average_yearly,
            'average_monthly': average_monthly,
            }

        return Response(data=data)
        
