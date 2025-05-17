from rest_framework.generics import ListAPIView


from products.models import Color
from products.api_endpoints.ColorList.serializers import ColorListSerializer


class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorListSerializer
    permission_classes = []
