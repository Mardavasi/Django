from django.db import models


# Modelo de Categorías
class Category(models.Model):
    # Campo para almacenar el nombre de la categoría
    name = models.CharField(max_length=255, verbose_name='Nombre')
    
    class Meta:
        # Configuración para la interfaz de administración
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']  # Ordenar las instancias por el campo 'name'
        
    def __str__(self):
        # Método que devuelve una representación en cadena del objeto (nombre de la categoría)
        return self.name


# Modelo de Productos
class Product(models.Model):
    # Opciones para el campo 'price_type'
    price_type_choices = (
        ('unitario','Precio unitario'),
        ('media-doc','Media docena'),
        ('docena','Docena'),
        ('por-kilo','Kilo')
    )
    
    # Campos para almacenar la información del producto
    name = models.CharField(max_length=255, verbose_name='Nombre')
    image = models.ImageField(upload_to='products/', default='imagen_default.png', verbose_name='Imagen')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_products', verbose_name='Categoría')
    description = models.TextField(verbose_name='Descripción') 
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    price_type = models.CharField(max_length=9, choices=price_type_choices,  default='unitario', verbose_name='Tipo de precio')
    
    class Meta:
        # Configuración para la interfaz de administración
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        # Método que devuelve una representación en cadena del objeto (nombre del producto)
        return self.name

    
