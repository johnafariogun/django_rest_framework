from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # discount = serializers.CharField(source = 'get_discount', read_only = True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    """
        OR
        my_discount = serializers.SerializerMethodField(read_only=True)
        then defining a method to return the `get_discount` method i.e
    """
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'type',
            'price',
            'content',
            'my_discount',
        ]
        """
            OR
        This returns discount as a field
        """
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
