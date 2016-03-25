from django.db import models

from .heroClasses import HeroClass

# skill of hero
class Ability(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    heroClass = models.ForeignKey(HeroClass, on_delete=models.CASCADE)
    cd = models.DurationField(default=0)
    #    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name