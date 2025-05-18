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
    path('categories/<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name="category-delete"),
    path('sizes/', SizeListAPIView.as_view(), name="size-list"),
    path('sizes/create/', SizeCreateAPIView.as_view(), name="size-create"),
    path('sizes/<int:pk>/', SizeRetrieveAPIView.as_view(), name="size-retrieve"),
    path('sizes/<int:pk>/update/', SizeUpdateAPIView.as_view(), name="size-update"),
    path('sizes/<int:pk>/delete/', SizeDeleteAPIView.as_view(), name="size-delete"),
    path('colors/', ColorListAPIView.as_view(), name="color-list"),
    path('colors/create/', ColorCreateAPIView.as_view(), name="color-create"),
    path('colors/<int:pk>/', ColorRetrieveAPIView.as_view(), name="color-retrieve"),
    path('colors/<int:pk>/delete/', ColorDeleteAPIView.as_view(), name="color-delete"),
    path('colors/<int:pk>/update/', ColorUpdateAPIView.as_view(), name="color-update"),
    path('brands/', BrandListAPIView.as_view(), name="brand-list"),
    path('brands/create/', BrandCreateAPIView.as_view(), name="brand-create"),
    path('brands/<str:slug>/', BrandRetrieveAPIView.as_view(), name="brand-retrieve"),
    path('brands/<str:slug>/update/', BrandUpdateAPIView.as_view(), name="brand-update"),
    path('brands/<int:pk>/delete/', BrandDeleteAPIView.as_view(), name="brand-delete"),
]