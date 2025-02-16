from rest_framework.views import APIView
from django.shortcuts import  render

class Sub(APIView):
    def get(self, request):
        print("GET")
        return render(request, "Jinstagram/main.html")

    def post(self, request):
        print("POST")
        return render(request,"Jinstagram/main.html")


