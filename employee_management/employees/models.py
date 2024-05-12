from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add more fields as needed

    
    def __str__(self):
        return self.name

class Meta:
        app_label = 'employees'