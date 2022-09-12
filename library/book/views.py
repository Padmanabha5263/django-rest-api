
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method=="POST"):
        serializer = BookSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"message":"Successfully book added"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
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
def authors(request):
    if(request.method=='GET'):
        author = models.Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method=='POST'):
        serializer = AuthorSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"message": "Author added successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
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
        return Response({"message":"author deleted successfully"},status=status.HTTP_200_OK)




@api_view(['GET', 'POST'])
def publications(request):
    if(request.method=='GET'):
        pub = models.Publication.objects.all()
        serializer = PublicationSerializer(pub, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if(request.method=='POST'):
        serializer = PublicationSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"message": "Publication added successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
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


