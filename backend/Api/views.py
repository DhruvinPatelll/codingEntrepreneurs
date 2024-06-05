from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import Product
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data,fields=['title','description','price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data, headers={"content_type": "application/json"})
