from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

from products.models import Brand
from products.api_endpoints.BrandCreate.serializers import BrandCreateSerializer

class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer
    parser_classes = [MultiPartParser]
    

