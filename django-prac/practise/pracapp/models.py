from django.db import models

# Create your models here.
class Contact(models.Model):
    usn=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=20,default="")
    sem=models.CharField(max_length=20,default="")
    phone=models.IntegerField()
    email=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name
    
