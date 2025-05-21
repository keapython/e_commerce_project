from rest_framework.generics import ListAPIView

from common.models import MediaFile
from common.api_endpoints.MediaFileList.serializers import MediaFileListSerializer

class MediaFileListAPIView(ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileListSerializer
    permission_classes = []
    
