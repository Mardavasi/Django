from rest_framework import serializers
from .models import  Category,Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','image','category','description','price','price_type')
        
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( '__all__')