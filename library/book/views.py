from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from .serializers import BookSerializer, AuthorSerializer, PublicationSerializer
# Create your views here.




@api_view(['GET'])
def books(request):
    books = models.Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookDetile(request, pk):
    books = models.Book.objects.get(pk=pk)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data)