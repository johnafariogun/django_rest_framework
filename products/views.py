from django.shortcuts import get_object_or_404
from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductMixinView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(Self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductDetailAPIView(generics.RetrieveAPIView): # default lookup_field is an integer i.e either id or pk
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    lookup_field = 'pk'  
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title #if no content save the title as the content

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    lookup_field = 'pk'  
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        


class ProductListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    def perform_create(self, serializer):

        name=serializer.validated_data.get('name')
        content=serializer.validated_data.get('content') or None

        if content is None:
            content = name
        
        serializer.save(content=content)


# to sue function-based views with rest_framework
@api_view(['GET', 'POST'])
def product_alt_view(request, pk, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            one = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(one).data
            return Response(data)           
        queryset = Product.object.all()
        data = ProductSerializer(queryset, many=True)
        # do a list one or all

    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)       
            return Response(serializer.data)
        return Response({"invalid":"invalid input"}, status=400)
