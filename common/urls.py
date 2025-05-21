from django.urls import path

from common.api_endpoints import *


urlpatterns = [
    path('mediafiles/', MediaFileListAPIView.as_view(), name="mediafile-list"),
    path('mediafiles/create/', MediaFileCreateAPIView.as_view(), name="mediafile-create"),
    path('mediafiles/<int:pk>/update/', MediaFileUpdateAPIView.as_view(), name="mediafile-update"),
    path('mediafiles/<int:pk>/delete/', MediaFileDeleteAPIView.as_view(), name="mediafile-delete"),
]

