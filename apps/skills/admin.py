from django.contrib import admin

from .models import *

admin.site.register(ProgrammingLanguage)
admin.site.register(LanguageType)
admin.site.register(Framework)
admin.site.register(AreaOfExpertise)