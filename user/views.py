from email.policy import default
import os
from uuid import uuid4
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

# Create your views here.
class join(APIView):
    def get(self,request):
        return render(request,"user/join.html")

    def post(self, request):  # 회원가입
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        name = request.data.get('name', None)
        nickname = request.data.get('nickname', None)


        # password 는 암호화 사용
        User.objects.create(email=email, password=make_password(password), name=name, nickname=nickname, profile_image=default)
        return Response(status=200)

class login(APIView):
    def get(self,request):
        return render(request,"user/login.html")
    def post(self,request):
        # 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = User.objects.filter(email=email).first() # 무조건 1개만  리턴 -> 바로 user사용 가능, user_list 사용 안해도 됨
        if user is None:
            return Response(status=404,data=dict(massage="회원정보가 잘못되었습니다."))
        if user.check_password(password):
            return Response(status=400)

class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")


class UploadProfile(APIView):
    def post(self, request):

        # 일단 파일 불러와
        file = request.FILES['file']
        email = request.data.get('email')

        uuid_name = uuid4().hex
        from Python_Insta_2.settings import MEDIA_ROOT
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name

        user = User.objects.filter(email=email).first()

        user.profile_image = profile_image
        user.save()

        return Response(status=200)