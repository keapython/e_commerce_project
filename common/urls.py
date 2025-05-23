from django.urls import path

from common.api_endpoints import *
from common.views import HomeView, ContactView, ShopDetailsView, ShopingCartView, CheckOutView, BlogDetailsView, ShopGridView, BlogView

app_name = "common"

urlpatterns = [
    path('mediafiles/', MediaFileListAPIView.as_view(), name="mediafile-list"),
    path('mediafiles/create/', MediaFileCreateAPIView.as_view(), name="mediafile-create"),
    path('mediafiles/<int:pk>/update/', MediaFileUpdateAPIView.as_view(), name="mediafile-update"),
    path('mediafiles/<int:pk>/delete/', MediaFileDeleteAPIView.as_view(), name="mediafile-delete"),
    path('index/', HomeView.as_view(), name="index"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('shop-details/', ShopDetailsView.as_view(), name="shop-details"),
    path('shoping-cart/', ShopingCartView.as_view(), name="shoping-cart"),
    path('check-out/', CheckOutView.as_view(), name="check-out"),
    path('blog-details/', BlogDetailsView.as_view(), name="blog-details"),
    path('shop-grid/', ShopGridView.as_view(), name="shop-grid"),
    path('blog/', BlogView.as_view(), name="blog"),
]

