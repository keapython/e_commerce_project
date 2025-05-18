from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Category
from products.api_endpoints.CategoryList.serializers import CategoryListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []

    def get (self, request, *args, **kwargs):
        print("[INFO][CategoryListAPIView]", request, args, kwargs)
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response (serializer.data)
    
class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []
    lookup_field = "slug"
    # lookup_field = "pk"  usually we search by pk, not by slug




    def get (self, request, *args, **kwargs):
        print("[INFO][CategoryRetrieveAPIView]", request, args, kwargs)
        # pk = kwargs.get('pk', None)
        # if pk is None:
        #     return Response ({"error": "Category id is required"}, status=400)
        serializer = self.serializer_class(self.get_object())

        return Response (serializer.data)


"""
lookup_field = "pk"

or we can write it ourselves:
       # pk = kwargs.get('pk', None)
        # if pk is None:
        #     return Response ({"error": "Category id is required"}, status=400) 

"""