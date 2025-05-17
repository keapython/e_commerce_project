from rest_framework.generics import DestroyAPIView

from products.models import Size
from products.api_endpoints.SizeDelete.serializers import SizeDeleteSerializer


class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeDeleteSerializer
    lookup_field = "slug"