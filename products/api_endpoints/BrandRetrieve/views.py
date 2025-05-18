from rest_framework.generics import RetrieveAPIView

from products.models import Brand
from products.api_endpoints.BrandRetrieve.serializers import BrandRetrieveSerializer

class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandRetrieveSerializer
    lookup_field = 'slug'
