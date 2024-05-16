from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from .import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# only reading the data
@api_view(['GET'])
def Booklist(request):
    books_obj = BooksModel.objects.all()
    serializer = BookSerializer(books_obj,many=True)
    return Response(serializer.data)
#Only posting the data  
@api_view(['POST'])
def Post_Book(request):
    books_obj = BooksModel.objects.all()
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
     


# Only for update data
@api_view(['POST'])
def Update_Book(request,id):
    books_obj = BooksModel.objects.get(id=id)
    serializer = BookSerializer(instance=books_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Only for delete the data
@api_view(['DELETE'])
def Delete_Book(request,id):
    books_obj = BooksModel.objects.get(id=id)
    books_obj.delete()
    
    return Response('<h3>Date was deleted at id matched</h3>')










