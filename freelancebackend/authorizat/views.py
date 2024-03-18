from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import generics,permissions
# Create your views here.




class Logout(APIView):
    def get(self,request,format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)