from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get-list -> queryset
    get-retrieve -> product instabce detail view
    post-create -> new instance
    put-update
    patch-partial update
    delete-destroy
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductGenericViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    get-list -> queryset
    get-retrieve -> product instabce detail view    
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'