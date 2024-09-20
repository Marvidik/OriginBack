from django.contrib import admin
from .models import Token,State,Numbers
# Register your models here.


admin.site.register(Token)
admin.site.register(Numbers)
admin.site.register(State)