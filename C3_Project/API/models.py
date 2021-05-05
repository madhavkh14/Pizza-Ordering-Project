from django.db import models

# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    
    TYPES = {
			('Regular', 'Regular'),
			('Square', 'Square'),
    }
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPES)
    toppings = models.ManyToManyField(Topping)
