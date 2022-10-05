from django.contrib import admin

from . models import Place
admin.site.register(Place)
# Register your models here.


from .models import Portfolio
admin.site.register(Portfolio)