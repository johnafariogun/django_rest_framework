from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer



# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    data=request.data
    # instance = Product.objects.all().order_by('?').first()
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        data=serializer.data
        print(data)
    return Response(data)

