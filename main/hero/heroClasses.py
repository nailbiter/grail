from django.db import models

# types of heroes. abilities depends on this
class HeroClass(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
#    portrait = models.ImageField(blank=True)
#    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name