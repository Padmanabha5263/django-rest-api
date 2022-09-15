from dataclasses import fields
from rest_framework import serializers
from . import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    book =BookSerializer(many=True, read_only=True)
    class Meta:
        model = models.Author
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    book =BookSerializer(many=True, read_only=True)
    class Meta:
        model = models.Publication
        fields = '__all__'