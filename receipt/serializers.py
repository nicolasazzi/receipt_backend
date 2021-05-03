from rest_framework import serializers

from .models import Receipt, Item
from account.models import Account


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['name', 'quantity', 'unit', 'price', 'category']

class GetReceiptSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True, source='item_set')

    class Meta:
        model = Receipt
        fields = ['purchase_date', 'total', 'items']

class CreateReceiptSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True, source='item_set')

    class Meta:
        model = Receipt
        fields = ['owner', 'total', 'purchase_date', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('item_set')
        receipt = Receipt.objects.create(**validated_data)

        for item_data in items_data:
            Item.objects.create(receipt=receipt, **item_data)

        return receipt
