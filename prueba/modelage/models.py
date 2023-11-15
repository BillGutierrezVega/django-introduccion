from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("el nombre del usuario", max_length=200)
    last_name = models.CharField("el apellido del usuario", max_length=200)
    car = models.ManyToManyField("Car", verbose_name="los carros del usuario")
    cell_phone = models.ManyToManyField("CellPhone", verbose_name="los números de contacto")

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not reviwed'),
    ('E', 'Error'),
    ('A', 'Acepted')
)

class Website(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    relese_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES ,max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} {self.rating}'
    
class Car(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    
class CellPhone(models.Model):
    number = models.CharField(max_length=15, primary_key=True)