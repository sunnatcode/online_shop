from django.shortcuts import render
from rest_framework.generics import( GenericAPIView, CreateAPIView, 
ListCreateAPIView, DestroyAPIView,ListAPIView,
 UpdateAPIView, RetrieveAPIView)
from .serializers import (CategorySerializers, ProductSerializers, 
CartSerializers, OrderSerializers, SearchProductSerializers, ProductDeleteSerializers)
from .models import Cart, Product, Category, Order
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.

class ProductView(GenericAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,]
    def post(self, request, *args, **kwargs):
        serializers = ProductSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            data = {
                'status':201,
                'success': True,
                'data':serializers.data
            }
            return Response(data, status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        data = Product.objects.all()
        serialziers = ProductSerializers(data, many=True)
        return Response(serialziers.data)


class CategoryView(ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        serializers = CategorySerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status.HTTP_201_CREATED)
        return Response({'message':'Something wrong'})    

    def get(self, request, *args, **kwargs):
        data = Category.objects.all()
        ser = CategorySerializers(data, many=True)
        return Response(ser.data)
    

class SearchProductView(GenericAPIView):
    serializer_class = SearchProductSerializers
    queryset = Product.objects.all()

    def post(self, request):
        post = self.queryset.filter(name=request.data.get('name'))
        ser = SearchProductSerializers(post, many=1)
        return Response(ser.data)


class CartView(GenericAPIView):
    serializer_class = CartSerializers
    queryset = Cart.objects.all()

    def post(self ,request, *args, **kwargs):
        serializers = CartSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        datta = Cart.objects.all()
        ser = CartSerializers(datta, many=True)
        return Response(ser.data)


class OrderView(GenericAPIView):
    serializer_class = OrderSerializers
    queryset = Order

    def post(self ,request, *args, **kwargs):
        ser = OrderSerializers(request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Order.objects.all()
        ser = OrderSerializers(data, many=True)
        return Response(ser.data)


class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductDeleteSerializers
    queryset = Product.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.delete()
            return Response({"message": 'Data deleted'})
        return Response(self.serializer_class().errors)


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializers(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "mobile number updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})












