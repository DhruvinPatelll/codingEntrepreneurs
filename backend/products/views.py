from django.dispatch import receiver
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description = title
        price = serializer.validated_data.get('price')
        serializer.save(description=description)
    
@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    if created:
        # Perform actions needed when a product is created
        print('****************')
        print('Product created!')
        print('****************')

# Connect the signal receiver
post_save.connect(create_product, sender=Product)

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk = pk)

product_detail_view = ProductDetailAPIView.as_view()