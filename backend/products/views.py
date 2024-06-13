from django.dispatch import receiver
from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Api.authentication import TokenAuthentication


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description") or None
        if description is None:
            description = title
        price = serializer.validated_data.get("price")
        instance = serializer.save(description=description)


@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    if created:
        print("****************")
        print("Product created!")
        print("****************")


post_save.connect(create_product, sender=Product)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk = pk)


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # Product.objects.get(pk = pk)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.descritption = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # Product.objects.get(pk = pk)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk = pk)


product_list_view = ProductListAPIView.as_view()
# class ProductMixinView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# product_mixin_view = ProductMixinView.as_view()

# @api_view(['GET','POST'])
# def product_alt_view(request,pk=None,*args,**kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             obj = get_object_or_404(Product,pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset,many=True).data
#         return Response(data)

#     if method == "POST":
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             description = serializer.validated_data.get('description') or None
#             if description is None:
#                 description = title
#             price = serializer.validated_data.get('price')
#             serializer.save(description=description)
#             return Response(serializer.data)
#         return Response({"invalid":"Not appropriate data"},status=400)
