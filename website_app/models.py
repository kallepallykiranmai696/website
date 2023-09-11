from django.db import models



# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    phone_number=models.BigIntegerField()
    email=models.EmailField()
    select_course=models.CharField(max_length=30)
    def __str__(self):
        return self.name
