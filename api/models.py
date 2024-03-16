from django.db import models

# Create your models here.


class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

class DocumentType(models.TextChoices):
    CC="CEDULA DE CIUDADANIA"  
    TI="TARJETA DE IDENTIDAD"

class Person(models.Model):
    document_type = models.CharField(max_length=100, choices=DocumentType.choices, default=DocumentType.CC)
    document = models.CharField(max_length=100, unique=True)
    names =  models.CharField(max_length=100)
    last_names=models.CharField(max_length=100)
    hobbie= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    deleted_at=models.DateTimeField(null=True, blank=True)
    
    