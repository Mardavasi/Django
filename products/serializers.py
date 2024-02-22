from rest_framework import serializers
from .models import  Category,Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','category','description','price')
        
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( '__all__')