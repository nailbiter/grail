from django.db import models

# gifts - just gifts form other users
class Gift(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    # tillDate = models.DateField()
    #    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name