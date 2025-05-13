from django.db import models

class LanguageType(models.Model):
    type_name = models.CharField(max_length=256)
    
class ProgrammingLanguage(models.Model):
    language_name = models.CharField(max_length=256)
    language_type = models.ForeignKey(LanguageType, on_delete=models.PROTECT)
