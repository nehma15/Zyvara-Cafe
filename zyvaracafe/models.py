from django.db import models

# Create your models here.

class Cake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cakes/')
    base_price = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return self.name
    

class CakeFlavour(models.Model):
    cake = models.ForeignKey(Cake,related_name='flavours',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class CakeSize(models.Model):
    cake = models.ForeignKey(Cake,related_name='sizes',on_delete=models.CASCADE)
    weight = models.CharField(max_length=50)
    extra_price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.weight
    


