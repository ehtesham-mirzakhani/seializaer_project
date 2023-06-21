from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializers
from .models import User


# Create your views here.

#get all user
@api_view(['GET'])
def getUser(request):
    users = User.objects.all()
    serializer = UserSerializers(users,many = True)
    return Response(serializer.data)

#get single user
@api_view(['GET'])
def getUser(request,pk):
    user = User.objects.get(id= pk)
    serializer = UserSerializers(user,many = False)
    return Response(serializer.data)

#add user
@api_view(['POST'])
def addUser(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update user
@api_view(['UPDATE'])
def updateUser(request,pk):
    user = User.objects.get(id = pk)
    serializer = UserSerializers(instance=user,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete user
@api_view(['DELETE'])
def deleteUser(request,pk):
    user = User.objects.get(id = pk)
    user.delete()
    return Response('item successfully deleted')

