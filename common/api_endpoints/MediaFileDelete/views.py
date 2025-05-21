from rest_framework.generics import DestroyAPIView

from common.models import MediaFile
from .serializers import MediaFileDeleteSerializer

class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer
    lookup_field = 'pk'