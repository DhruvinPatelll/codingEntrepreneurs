from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Product
        fields = ["edit_url","url","pk", "title", "owner", "description", "price", "sale_price", "discount"]

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(self, Product):
            return None
        return obj.get_discount()

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        user = request.user
        if user.has_perm('products.change_product'):
            return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)