from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product
from .serializers import categorySerializer, ProductSerializer




# creamos una sola vista para cada modelo se usan estas clases viewsets ya que son mas flexibles en comparacion de  las generics views
class productViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False)
    def by_category(self, request):
        category = self.request.query_params.get('category', None)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class categoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categorySerializer



