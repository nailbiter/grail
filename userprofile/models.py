from django.db import models
from main.projectUser.models import ProjectUser

class ProfileName(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(ProjectUser)