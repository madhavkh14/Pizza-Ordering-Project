# Generated by Django 3.1.7 on 2021-05-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]