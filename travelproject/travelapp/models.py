from django.db import models

# Create your models here.
class  Place(models.Model):
     name=models.CharField(max_length=250)
     image=models.ImageField(upload_to='pics')
     descp=models.TextField()

     def __str__(self):
          return self.name


class  Portfolio(models.Model):
     name=models.CharField(max_length=250)
     image=models.ImageField(upload_to='picss')
     descp=models.TextField()

     def __str__(self):
          return self.name