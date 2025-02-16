from django.db import models

class Feed(models.Model):
    content = models.TextField()  # 글 내용
    image = models.ImageField(upload_to='feeds/')  # 피드 이미지 (업로드 경로 지정)
    profile_image = models.ImageField(upload_to='profiles/')  # 프로필 이미지
    user_id = models.TextField()  # 글쓴이
    like_count = models.IntegerField()  # 좋아요 수
