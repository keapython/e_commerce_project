from rest_framework.generics import UpdateAPIView
# from rest_framework.parsers import MultiPartParser, FormParser

from products.models import Brand
from products.api_endpoints.BrandUpdate.serializers import BrandUpdateSerializer

class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer
    # parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'slug'