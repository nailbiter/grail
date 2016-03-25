from django.db import models

# just technical table, list of types: leg, head, right arm, etc..
class EquipmentType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

# equipment of hero
class Equipment(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
#    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name