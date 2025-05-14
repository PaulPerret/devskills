from django.db import models

class LanguageType(models.Model):
    type_name = models.CharField("Type", max_length=256)
    def __str__(self):
        return self.type_name
 
class ProgrammingLanguage(models.Model):
    language_name = models.CharField("Name", max_length=256)
    language_type = models.ForeignKey(LanguageType, on_delete=models.PROTECT)
    def __str__(self):
        return self.language_name

class Framework(models.Model):
    framework_name = models.CharField("Name", max_length=256)
    def __str__(self):
        return self.framework_name

class AreaOfExpertise(models.Model):
    aoe_name = models.CharField("Name", max_length=256)
    def __str__(self):
        return self.aeo_name

