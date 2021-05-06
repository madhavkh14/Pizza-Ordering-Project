from django.db import models

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    
    TYPES = {
			('Regular', 'Regular'),
			('Square', 'Square'),
    }
    size = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=TYPES, blank=True)
    toppings = models.CharField(max_length=150, blank=True)
