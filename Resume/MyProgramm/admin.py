from django.contrib import admin
from .models import Text
from .models import Word
from .models import TextFormat

admin.site.register(Text)
admin.site.register(Word)
admin.site.register(TextFormat)
