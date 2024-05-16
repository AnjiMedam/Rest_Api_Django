from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from .import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Only for reading the data
@api_view(['GET'])
def Movielist(request):
    movie_data = MovieModel.objects.all()
    serializer = MovieSerializer(movie_data,many=True)
    return Response(serializer.data)

    #Only for posting the data 
@api_view(['POST'])
def Post_movie(request):
    # movie_data = MovieModel.objects.all()
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Only for updating the data
@api_view(['POST'])
def Update_movie(request,id):
    movie_data = MovieModel.objects.get(id=id)
    serializer = MovieSerializer(instance=movie_data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# Only deleting the data
@api_view(['DELETE'])
def Delete_movie(request,id):
    movie_data = MovieModel.objects.get(id=id)
    # serializer = MovieSerializer(movie_data,many=True)
    movie_data.delete()
    return Response('i was deleted data when id exist in model..!')




