from django.db import models
from django.contrib.auth.models import User
from skills.models import Skill

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)

    # class Meta:
    #     app_label = 'employees.Employee'

    def __str__(self):
        return self.user.get_full_name() or self.user.username