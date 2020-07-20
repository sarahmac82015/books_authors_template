from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now= True)

class Author(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name = 'authors')
    notes = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now= True)

@property
def full_name(self):
    return f"{self.first_name} {self.last_name}"
