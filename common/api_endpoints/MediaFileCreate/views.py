from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser


from common.models import MediaFile
from common.api_endpoints.MediaFileCreate.serializers import MediaFileCreateSerializer

class MediaFileCreateAPIView(CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer
    parser_classes = [MultiPartParser, FormParser]

    