from django.urls import path
from .views import join,login, LogOut, UploadProfile

urlpatterns = [
    path('join', join.as_view()),
    path('login', login.as_view()),
    path('logout', LogOut.as_view()),
    path('profile/upload', UploadProfile.as_view())
]