from django.db import models

class AchievementType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

# classic badge. have conditions and profit)
class Achievement(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    type = models.ForeignKey(AchievementType, on_delete=models.CASCADE)
    #    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name