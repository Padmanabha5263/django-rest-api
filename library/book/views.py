
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from .serializers import BookSerializer, AuthorSerializer, PublicationSerializer
# Create your views here.




@api_view(['GET', 'POST'])
def books(request):
    if(request.method == "GET"):
        books = models.Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def bookDetile(request, pk):
    try:
        books = models.Book.objects.get(pk=pk)
        serializer = BookSerializer(books, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except models.Book.DoesNotExist:
        return Response({"message":"book does not exist"}, status=status.HTTP_404_NOT_FOUND)
    




@api_view(['GET'])
def authors(request):
    author = models.Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def author(request, pk):
    try:
        author = models.Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except models.Author.DoesNotExist:
        return Response({"message":"Author doesn't exist"}, status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def publications(request):
    pub = models.Publication.objects.all()
    serializer = PublicationSerializer(pub, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def publication(request, pk):
    try:
        pub = models.Publication.objects.get(pk=pk)
        serializer = PublicationSerializer(pub, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except models.Publication.DoesNotExist:
        return Response({"message":"Publication doesn't exist"}, status=status.HTTP_404_NOT_FOUND)