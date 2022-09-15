from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Author(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobileNum =models.BigIntegerField()
    email = models.EmailField(max_length=60)
    dob = models.DateField()
    address = models.CharField(max_length=80)
    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    isAlive = models.BooleanField(default=True)

    class Meta:
        db_table='library_Authors'

    def __str__(self):
        return f'fname = {self.fname}, lname={self.lname}'


class Publication(models.Model):
    name = models.CharField(max_length=40)
    addresss = models.CharField(max_length=80)
    mobileNum = models.BigIntegerField()
    email =  models.EmailField(max_length=60)
    website = models.CharField(max_length=40, null=True)
    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table='library_Publications'

    def __str__(self):
        return f'name = {self.name}'



class Book(models.Model):
    name = models.CharField(max_length=30)
    discription = models.CharField(max_length=100)
    authorId = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    publicationId = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='book')
    dateTimeCreated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table='library_Books'

    def __str__(self):
        return f'name = {self.name}'





