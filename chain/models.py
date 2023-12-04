from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)


class Product(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    release_date = models.DateField()


class Chain(MPTTModel):
    title = models.CharField(max_length=50)
    duty = models.FloatField(max_length=256)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    date_of_chenge = models.DateField()
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE, related_name='продукты')


    def __str__(self):
        return f'{self.title}'

    class MPTTMeta:
        order_insertion_by = ['title']