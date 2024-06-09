from rest_framework import serializers, viewsets

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'discount_price',
            'discount',
        ]

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount_val()
        #try:
        #    return obj.get_discount_val()
        #except:
        #    return None