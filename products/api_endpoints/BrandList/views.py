from rest_framework.generics import ListAPIView

from products.models import Brand
from products.api_endpoints.BrandList.serializers import BrandListSerializer


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = []
  