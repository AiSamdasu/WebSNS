import os

from uuid import uuid4
from content.models import Feed
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Feed

# Create your views here.
class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed; -는 역순으로 출력
        return render(request, "Jinstagram/main.html", context=dict(feeds=feed_list))

class UploadFeed(APIView):
    def post(self,request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        from Python_Insta_2.settings import MEDIA_ROOT
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        # 파일 읽어서 파일로 만들때 사용
        with open(save_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)


        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0)

        return Response(status=200)