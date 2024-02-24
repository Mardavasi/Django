from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import  Category,Product

# Clase para filtrar productos por categoría, precio y nombre
class ProductFilter(filters.FilterSet):
    # Variable para filtrar por categoría utilizando el id exacto
    category = filters.NumberFilter(field_name='category', lookup_expr='exact') 
    # Variable para filtrar por nombre, buscando coincidencias parciales
    name = filters.CharFilter(method='filter_by_search', lookup_expr='icontains')    
    
    # Método para realizar el filtrado por nombre y descripción
    def filter_by_search(self, queryset, value):
        return queryset.filter(name__icontains=value) | queryset.filter(description__icontains=value)
    
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'name': ['icontains'],
        }

# Serializador para productos
class ProductSerializer(serializers.ModelSerializer):
    # Campo adicional para mostrar el nombre de la categoría en lugar del id
    category_name = serializers.ReadOnlyField(source='category.name')
    # Campo adicional para mostrar la descripción del tipo de precio
    price_type_description = serializers.ReadOnlyField(source='get_price_type_display')
    
    class Meta:
        model = Product
        # Campos a incluir en la serialización
        fields = ('id', 'name', 'image', 'category', 'category_name', 'description', 'price', 'price_type', 'price_type_description')
        # Especifica la clase de filtro asociada
        filterset_class = ProductFilter

# Serializador para categorías
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
