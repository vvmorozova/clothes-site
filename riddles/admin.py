from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Option, Riddle

admin.site.register(Riddle)
admin.site.register(Option)

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

from .models import Item, Pics, Composition

admin.site.register(Item)
admin.site.register(Pics)
# admin.site.register(Sizes)
admin.site.register(Composition)