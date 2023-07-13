from django.db import models

# Create your models here.
# class Category(models.Model):
#     pass


class DemoModel(models.Model):
   title = models.CharField(max_length=255)
   price = models.DecimalField(decimal_places=5, max_digits=10)
   description = models.CharField(max_length=500)
   
   def __str__(self) -> str:
      return self.title
'''
{
    "title": "Malware Analysis all in one"
    "price": "100",
    "description": "Malware Analysis all in one description"
}



'''