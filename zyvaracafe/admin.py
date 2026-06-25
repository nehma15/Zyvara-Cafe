from django.contrib import admin
from .models import Cake, CakeFlavour, CakeSize

# Register your models here.

admin.site.register(Cake)
admin.site.register(CakeFlavour)
admin.site.register(CakeSize)
