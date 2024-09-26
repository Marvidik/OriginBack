from django.contrib import admin
from .models import Token,State,StateCode,Phrases
# Register your models here.


admin.site.register(Token)
admin.site.register(State)
admin.site.register(StateCode)
admin.site.register(Phrases)