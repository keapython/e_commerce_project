from rest_framework.generics import ListAPIView, RetrieveAPIView

from products.models import Size
from products.api_endpoints.SizeList.serializers import SizeListSerializer


class SizeListAPIView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    permission_classes = []


class SizeRetrieveAPIView(RetrieveAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeListSerializer
    permission_classes = []
    lookup_field = "slug"
    
