from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import  Category,Product

#se crea la clase ProductFilter para poder filtrar los productos por categoria, precio y nombre
class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
        }




class ProductSerializer(serializers.ModelSerializer):
    #se agrega el campo category_name y price_type_description para que se muestre el nombre de la categoria en vez del id
    category_name= serializers.ReadOnlyField(source='category.name')
    price_type_description= serializers.ReadOnlyField(source='get_price_type_display')
    class Meta:
        model = Product
        fields = ('id', 'name','image','category','category_name','description','price','price_type','price_type_description')
        filterset_class = ProductFilter
        
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( '__all__')