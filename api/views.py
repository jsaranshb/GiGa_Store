from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework import status
from user_profile.models import UserModel
from .import serializers
from product.models import Product, ProductCategory
from cart.models import Cart
from payment.models import PaymentDetails
from order.models import Order, OrderDetails


class ProductCategoryView(ModelViewSet):
    http_method_names = ['get']
    serializer_class = serializers.ProductCategorySerializer
    queryset = ProductCategory.objects.filter(status=True)


class ProductView(ModelViewSet):
    http_method_names = ['get']
    queryset = Product.objects.filter(status=True)
    serializer_class = serializers.ProductSerializer

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return serializers.ProductDetailedSerializer
        return self.serializer_class

    def list(self, request):
        filterDict = {
            'status' : True,
        }
        if request.GET.get('category_id'):
            filterDict['product_category_id'] = request.GET.get('category_id')
        if request.GET.get('search'):
            filterDict['name__contains'] = request.GET.get('search')
        queryset1 = Product.objects.filter(**filterDict)
        serializer = self.serializer_class(queryset1, many=True)
        return Response(serializer.data)
        

class CostumerView(ModelViewSet):
     serializer_class = serializers.CostumerSerializer
     queryset = User.objects.filter(is_superuser=False, is_staff=False)


class LoginUserView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CartSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data.get('quantity')
            product = serializer.validated_data.get('product')
            cart, _ = Cart.objects.get_or_create(user=request.user, product=product)
            if int(quantity) == 0:
                cart.delete()
            else:
                cart.quantity = quantity  
                cart.save()
            return Response({'Message' : 'Success'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
 
    def delete(self, request, id=None):
        if id:
            cart = Cart.objects.filter(id=id)
            cart.delete()
            return Response({'Message' : 'Successfully Deleted.'})
        return Response({'Message' : 'Please provide expected ID to delete any item form Cart.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
 

class CheckOutView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.PaymentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            paymentId = serializer.validated_data.get('payment_id')
            transactionId = serializer.validated_data.get('transaction_id')
            PaymentDetails.objects.create(payment_id=paymentId, transaction_id=transactionId)
            order = Order.objects.create(user=request.user, date_time=datetime.now())
            carts = Cart.objects.filter(user=request.user)
            for cart in carts:
                OrderDetails.objects.create(
                    order=order,
                    product=cart.product,
                    quantity=cart.quantity,
                    price=cart.product.price
                )
                cart.delete()
            return Response({'order_id' : order.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeliveryDetailsView(ModelViewSet):
    serializer_class = serializers.DeliverySerializer
    queryset = UserModel.objects.all()


class OrderView(ModelViewSet):
    http_method_names = ['get']
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.OrderSerializer
    queryset = OrderDetails.objects.all()

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return serializers.OrderDetailsSerializer
        return self.serializer_class

