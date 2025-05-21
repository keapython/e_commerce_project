from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from common.models import MediaFile
from common.api_endpoints.MediaFileUpdate.serializers import MediaFileUpdateSerializer


class MediaFileUpdateAPIView(UpdateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileUpdateSerializer
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = "pk"