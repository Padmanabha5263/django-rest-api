from django.db import models

# Create your models here.
class Author(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobileNum =models.BigIntegerField()
    email = models.EmailField(max_length=60)
    dob = models.DateField()
    address = models.CharField(max_length=80)
    isAlive = models.BooleanField(default=True)

    def __str__(self):
        return f'fname = {self.fname}, lname={self.lname}'


class Publication(models.Model):
    name = models.CharField(max_length=40)
    addresss = models.CharField(max_length=80)
    mobileNum = models.BigIntegerField()
    email =  models.EmailField(max_length=60)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f'name = {self.name}'


class Book(models.Model):
    name = models.CharField(max_length=30)
    discription = models.CharField(max_length=100)
    authorId = models.ForeignKey(Author, on_delete=models.CASCADE)
    publicationId = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def __str__(self):
        return f'name = {self.name}'




