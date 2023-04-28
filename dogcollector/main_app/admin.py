from django.contrib import admin
# import your models here
from .models import Dog, Feeding, Toy 

# Register your models here
admin.site.register(Dog)
# register the new Feeding Model
admin.site.register(Feeding)
admin.site.register(Toy)