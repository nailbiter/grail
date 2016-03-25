from django.db import models

# Goal - public global goal of user
class Goal(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    tillDate = models.DateField()

    def __str__(self):
        return self.name