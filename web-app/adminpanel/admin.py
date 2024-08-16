from django.contrib import admin
from .models import *

# Register your models here.
class TypeAdmin():
    pass 
    admin.site.register(Type)

class TypeOffice():
    pass 
    admin.site.register(Office)

class TypeDevice():
    pass 
    admin.site.register(Device)

class TypeClientRole():
    pass 
    admin.site.register(ClientRole)

class TypeClient():
    pass 
    admin.site.register(Client)

class TypeEntry():
    pass 
    admin.site.register(Entry)