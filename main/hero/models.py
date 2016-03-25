from django.db import models
from django.utils import timezone

from .abilities import Ability, HeroClass
from .equipment import Equipment

class Hero(models.Model):
    name = models.CharField(max_length=30)
    heroClass = models.ForeignKey(HeroClass, on_delete=models.CASCADE)
    abilities = models.ManyToManyField(Ability, through='AbilityOwn', symmetrical=False)
    equipment = models.ManyToManyField(Equipment, through='EquipmentOwn', symmetrical=False)

    def __str__(self):
        return self.name

class EquipmentOwnType(models.Model):
    name = models.CharField(max_length=30)

class EquipmentOwn (models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    type = models.ForeignKey(EquipmentOwnType)

    class Meta:
        unique_together=('hero', 'equipment')

class AbilityOwnType(models.Model):
    name = models.CharField(max_length=30)

class AbilityOwn(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    type = models.ForeignKey(AbilityOwnType)
    lastTimeUsed = models.DateTimeField(default=None)

    def use(self):

        def cast(self):

            def first_ability():
                return ('we used first ability')

            def second_ability():
                return ('we used second ability')

            options = {
                'firstAbility' : first_ability,
                'secondAbility' : second_ability,
            }
            try:
                options[self.ability.name]
            except:
                return ('no such ability')

        if ((timezone.now()-self.ability.cd)>self.lastTimeUsed):
            cast()
            self.lastTimeUsed = timezone.now()
        else:
            return ('you cant use ability right now, please wait')

    class Meta:
        unique_together=('hero', 'ability')