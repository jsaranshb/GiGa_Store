from django.contrib.auth.models import User
from rest_framework import serializers
from order.models import Order, OrderDetails
from product.models import Product, ProductCategory, ProductImages
from cart.models import Cart
from user_profile.models import UserModel


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']


class ProductDetailedSerializer(serializers.ModelSerializer):
    ProductImages = ProductImagesSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'cover_image']


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, user_object, validated_data):
        if validated_data.get('username'):
            user_object.username = validated_data.get('username',user_object.username)
        if validated_data.get('first_name'):
            user_object.first_name = validated_data.get('first_name',user_object.first_name)
        if validated_data.get('last_name'):    
            user_object.last_name = validated_data.get('last_name',user_object.last_name)
        if validated_data.get('email'):    
            user_object.email = validated_data.get('email',user_object.email)
        if validated_data['password']:
            user_object.set_password(validated_data['password'])
        user_object.save()
        return validated_data


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']
        

class PaymentSerializer(serializers.Serializer):

    payment_id = serializers.CharField(max_length=80)
    tarnsaction_id = serializers.CharField(max_length=150)


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['user', 'address', 'mobile']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ['order']
        depth = 1


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'
        depth = 1
        
