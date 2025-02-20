
from django.urls import path,include

from .settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from .views import Sub
from content.views import Main, UploadFeed
from django.conf import settings

urlpatterns = [
    path('',Main.as_view()),
    # path('content/upload', UploadFeed.as_view()),
path('main', Main.as_view(), name='main'),  # /main 경로 추가
    path('content/',include('content.urls')),
path('user/',include('user.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

