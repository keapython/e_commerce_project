from rest_framework.generics import RetrieveAPIView

from products.models import Color
from products.api_endpoints.ColorRetrieve.serializers import ColorRetrieveSerializer



class ColorRetrieveAPIView(RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorRetrieveSerializer
    lookup_field = "pk"