# Pizza-Ordering-Project
This project allows user to order Pizza with specific Size, Type and Any Toppings. This Project uses `Django-rest-framework` to handle CRUD operations and uses MongoDB Atlas as the database to store the data.

# Requirements
The following packages are required for this project:

* appdirs==1.4.4
* asgiref==3.3.1
* distlib==0.3.1
* Django==3.1.7
* django-filter==2.4.0
* djangorestframework==3.12.4
* djongo==1.3.4
* dnspython==2.1.0
* filelock==3.0.12
* importlib-metadata==3.8.0
* mysqlclient==2.0.3
* pymongo==3.11.4
* pytz==2021.1
* six==1.15.0
* sqlparse==0.2.4
* typing-extensions==3.7.4.3
* virtualenv==20.4.3
* irtualenvwrapper-win==1.2.6
* zipp==3.4.1

# Installation

Install REST FRAMEWORK using `pip`...

    pip install djangorestframework

Add `'rest_framework'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]
    
Install Django Filters using `pip`...
    
    pip install django_filters
    
 # About the Project
 
 
### Creating Models
 
 First, making the models in `models.py` file inside the django-app `API`
 
 ```python
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
```
Note: Although the user cannot choose a `size` outside of the database, we can also use the `ForeignKey` field. Here, I've used validation in the serializer class.

### Creating Serializer Classes

Making Serializer class in `serializers.py` file inside the django-app `API`

```python
from rest_framework import serializers
from .models import *

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id','size','type','toppings']

    # Field level Validation
    def validate_type(self, value):
        value=value.title()
        if value == 'Regular' or value == 'Square':
            return value
        else:
            raise serializers.ValidationError('Wrong type entered!!')

    def validate_size(self, value):
        value=value.title()
        if Size.objects.filter(name=value).exists():
            return value
        else:
            raise serializers.ValidationError('The given size is incorrect!!')
```
In this Serializer class, I have used `ModelSerializer` which automatically creates all the CRUD functions. I have alsou sed field level validation to check that the user only enters the input under the given constraints, i.e. 
* The type of the pizza can only be 'Regular' or 'Square'
* The size of the pizza should be in the database else there should be an error

### Defining Views

Creating Veiw classes using `GenericAPIView` classes in `views.py` file inside the django-app `API`

```python
class CreatePizza(CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
```
Created `CreatePizza` API which inherits `CreateAPIView` class to handle POST requests. It takes JSON format data and creates an object of the model `Pizza` using the `PizzaSerializer` class.
The input format of this class can be seen in the screenshot

![image](https://user-images.githubusercontent.com/77589071/117285033-259f1c80-ae85-11eb-814d-9db14f774db2.png)


Now, the `ListPizza` API class is described as

```python
class ListPizza(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type','size']
```
Created `ListPizza` API which inherits `ListAPIView` class to handle GET requests. It returns the list of the objects in JSON format using the `PizzaSerializer` class. I have also used `DjangoFilterBackend` library to filter the queryset based on the fields mentioned in the `filterset_fields` parameter. 
The returned list format can be seen in the screenshot

![image](https://user-images.githubusercontent.com/77589071/117286030-516ed200-ae86-11eb-9bbe-7420aeaf2835.png)


The `EditPizza` API class is described as 

```python
class EditPizza(RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
```
Created `EditPizza` API which inherits `RetrieveUpdateDestroyAPIView` class to handle GET, PUT and DELETE requests. It returns a specific object in the model which is `Pizza` in this case, and can update and delete the object.
The returned response can be seen in the screenshot

![image](https://user-images.githubusercontent.com/77589071/117287082-96473880-ae87-11eb-9cc7-248e6078d74c.png)


### Defining Routes

Mapping the routes to the view functions in `urls.py` file

```python
from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_pizza/',views.ListPizza.as_view(), name="list-pizza"),
    path('create_pizza/',views.CreatePizza.as_view(), name="create-pizza"),
    path('edit_pizza/<str:pk>',views.EditPizza.as_view(), name="edit-pizza"),
]
```
Creating three extra routes for three APIs defined above.

# How to run the Project

Create a New folder and open the terminal in the Folder and execute the following commands

    git clone https://github.com/madhavkh14/Pizza-Ordering-Project.git
    cd C3Project
    python manage.py runserver
    
Now the project will be running on `localhost:8000` or `http://127.0.0.1:8000/`. Follow the given routes in Defining Routes section to execute the required APIs.
