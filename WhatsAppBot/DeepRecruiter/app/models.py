from django.db import models

class Provider(models.Model):
    full_name = models.CharField(max_length=30)
    id_no = models.CharField(max_length=13)
    abilities = models.CharField(max_length=500)
    skills = models.CharField(max_length=500)
    interests = models.CharField(max_length=500)
    hobbies = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)