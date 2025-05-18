from rest_framework.generics import DestroyAPIView

from products.models import Brand
from products.api_endpoints.BrandDelete.serializers import BrandDeleteSerializer

class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDeleteSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        print(request, args, kwargs)
        return super().delete(request, *args, **kwargs)