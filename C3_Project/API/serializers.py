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


