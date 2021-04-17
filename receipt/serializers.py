from rest_framework import serializers

from .models import Receipt, Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['name', 'quantity', 'unit', 'price', 'category']

class ReceiptSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True, source='item_set')

    class Meta:
        model = Receipt
        fields = ['purchase_date', 'total', 'items']