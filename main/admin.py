from django.contrib import admin
from .models import ToDoList, Item, Ksiazka, Zamowienie, User
# Register your models here.

#admin.site.register(ToDoList)
#admin.site.register(Item)
admin.site.register(User)
admin.site.register(Ksiazka)
admin.site.register(Zamowienie)
#admin.site.register(Profile)