from rest_framework import serializers
from .models import Cart, Category, Product, Order
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
class CartSerializers(serializers.ModelSerializer):
    def validate(self, data):
        if not User.objects.filter(id=data['user_id']).exists:
            raise ValidationError('This user not exists')
        return data
    class Meta:
        fields = '__all__'
        model = Cart

class CategorySerializers(serializers.ModelSerializer):
    def validate(self, data):
        if Category.objects.filter(name=data['name']).exists():
            raise ValidationError('This category already exists')
        return data
    class Meta:
        fields = '__all__'
        model = Category

class ProductSerializers(serializers.ModelSerializer):
    def validate(self, data):
        if Product.objects.filter(name=data['name']).exists():
            raise ValidationError('This product already exists')

        # if not Category.objects.filter(id=data['category']).exists():
            # raise ValidationError('This category id not found ')
        return data
    class Meta:
        fields = '__all__'
        model = Product

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Order

    def validate(self, data):
        if not Cart.objects.filter(id=data['cart_id']).exists():
            raise ValidationError('This car not founf')

        if not Product.objects.filter(id=data['product_id']).exists():
            raise ValidationError('This product not found')
        return data

class SearchProductSerializers(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(max_length=200)
    price       = serializers.FloatField()
    image = serializers.FileField()
    def validate(self, data):
        if not Product.objects.filter(name=self.name).exists():
            raise ValidationError('This product not found')
        return data
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class ProductDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        print(data)
        if not Product.objects.filter(id=data).exists():
            raise ValidationError("This product not exists")