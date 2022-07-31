from .import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pCategory', views.ProductCategoryView)
router.register('product', views.ProductView)
router.register('costumer', views.CostumerView)
router.register('delivery_details/', views.DeliveryDetailsView)
router.register('orders', views.OrderView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginUserView.as_view()),
    path('usercart/', views.CartView.as_view()),
    path('usercart/<id>/', views.CartView.as_view()),
    path('checkout/', views.CheckOutView.as_view()),
]
