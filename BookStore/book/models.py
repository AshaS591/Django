from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authour = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    published_date = models.DateField()
    description = models.TextField()
    def __str__(self):
        return self.title
