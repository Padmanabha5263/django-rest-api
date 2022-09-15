
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from . import models
from .serializers import BookSerializer, AuthorSerializer, PublicationSerializer
from .permissions import AdminOrReadOnly
# Create your views here.




@api_view(['GET', 'POST'])
@permission_classes([AdminOrReadOnly])
def books(request):
    if(request.method == "GET"):
        books = models.Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method=="POST"):
        serializer = BookSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AdminOrReadOnly])
def bookDetile(request, pk):
    try:
        books = models.Book.objects.get(pk=pk)
    except models.Book.DoesNotExist:
        return Response({"message":"book does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if(request.method=='GET'):
        serializer = BookSerializer(books, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method=='PUT'):
        serializer = BookSerializer(books,data=request.data)
        if(serializer.is_valid()): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    if(request.method=='DELETE'):
        books.delete()
        return Response({"message":"book deleted successfully"}, status=status.HTTP_200_OK) 




@api_view(['GET', 'POST'])
@permission_classes([AdminOrReadOnly])
def authors(request):
    if(request.method=='GET'):
        author = models.Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method=='POST'):
        serializer = AuthorSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AdminOrReadOnly])
def author(request, pk):
    try:
        author = models.Author.objects.get(pk=pk)
    except models.Author.DoesNotExist:
        return Response({"message":"Author doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    if(request.method=='GET'):
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if(request.method=='PUT'):
        serializer=AuthorSerializer(author, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if(request.method=='DELETE'):
        author.delete()
        return Response({"message":"Author deleted successfully"},status=status.HTTP_200_OK)




@api_view(['GET', 'POST'])
@permission_classes([AdminOrReadOnly])
def publications(request):
    if(request.method=='GET'):
        pub = models.Publication.objects.all()
        serializer = PublicationSerializer(pub, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method=='POST'):
        serializer = PublicationSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AdminOrReadOnly])
def publication(request, pk):
    try:
        pub = models.Publication.objects.get(pk=pk)
    except models.Publication.DoesNotExist:
        return Response({"message":"Publication doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    if(request.method=='GET'):
        serializer = PublicationSerializer(pub, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if(request.method=='PUT'):
        serializer=PublicationSerializer(pub, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if(request.method=='DELETE'):
        pub.delete()
        return Response({"message":"publication deleted successfully"},status=status.HTTP_200_OK)


