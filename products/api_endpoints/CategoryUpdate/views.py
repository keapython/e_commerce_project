from rest_framework.generics import UpdateAPIView

from products.models import Category
from products.api_endpoints.CategoryUpdate.serializers import CategoryUpdateSerializer


class CategoryUpdateAPIView(UpdateAPIView):
    # http_method_names = ["patch"]    if i write this it will show only patch api in swagger
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field = "slug"


