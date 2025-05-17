from django.urls import path

from products.api_endpoints import *


urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name="product-list1"),
    path('list2/', ProductListAPIView2.as_view(), name="product-list2"),
    path('list3/', ProductListAPIView3.as_view(), name="product-list3"),
    path('list4/', ProductListAPIView4.as_view(), name="product-list4"),
    path('categories/', CategoryListAPIView.as_view(), name="category-list"),
    path('categories/create/', CategoryCreateAPIView.as_view(), name="category-create"),
    path('categories/<str:slug>/', CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    # path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    path('categories/<str:slug>/update/', CategoryUpdateAPIView.as_view(), name="category-update"),
    path('categories/<str:slug>/delete/', CategoryDeleteAPIView.as_view(), name="category-delete"),
    path('sizes/', SizeListAPIView.as_view(), name="size-list"),
    path('sizes/create/', SizeCreateAPIView.as_view(), name="size-create"),
    path('sizes/<str:slug>/', SizeRetrieveAPIView.as_view(), name="size-retrieve"),
    path('sizes/<str:slug>/update/', SizeUpdateAPIView.as_view(), name="size-update"),
    path('sizes/<str:slug>/delete/', SizeDeleteAPIView.as_view(), name="size-delete"),
    path('colors/', ColorListAPIView.as_view(), name="color-list"),
    path('colors/create/', ColorCreateAPIView.as_view(), name="color-create"),
    path('colors/<str:slug>/delete/', ColorDeleteAPIView.as_view(), name="color-delete"),
    path('colors/<str:slug>/update/', ColorUpdateAPIView.as_view(), name="color-update"),

]