from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import storeSerializer
from .models import Store
import datetime

@api_view(['GET'])
def index(request):

    return render(request,'fiverr.html', {})

@api_view(['GET'])
def itemdetail(request):
    
    data = Store.objects.all()
    serializer = storeSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def aitemdetail(request,pk):
    data = Store.objects.get(pk=pk)
    serializer = storeSerializer(data,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def itemadd(request):
    
    serializer = storeSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def aitemupdate(request,pk):
    data = Store.objects.get(pk=pk)
    serializer = storeSerializer(data,request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def itemdelete(request,pk):
    data = Store.objects.get(pk=pk)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)