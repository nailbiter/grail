from django.db import models
from django.contrib.auth.models import User

from .achievements import Achievement
from main.hero.models import Hero

class ProjectUser(models.Model):
    login = models.OneToOneField(User, default=None)
    nickname = models.CharField(max_length=30)
    # sex = models.BooleanField()
    dateOfBirth = models.DateField()
    friends = models.ManyToManyField('self',through='UserM2MUser', symmetrical=False)

    hero=models.OneToOneField(Hero, blank=True)

    coins = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    creativity = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    willpower = models.IntegerField(default=0)
    coaching = models.IntegerField(default=0)
    nobility = models.IntegerField(default=0)
    kindness = models.IntegerField(default=0)

    achievements = models.ManyToManyField(Achievement, through='UserM2MAchievement', symmetrical=False)


    def __str__(self):
        return self.nickname

class AchievementOwnType (models.Model):
    name = models.CharField(max_length=30, default=None)

class UserM2MAchievement(models.Model):
    owner = models.ForeignKey(ProjectUser)
    achievement = models.ForeignKey(Achievement)
    date = models.DateField(default=None)
    type = models.ForeignKey(AchievementOwnType)

    class Meta:
        unique_together=('owner','achievement')

class RelationType(models.Model):
    name = models.CharField(max_length=30, default=None)

class UserM2MUser (models.Model):
    fromFriend = models.ForeignKey(ProjectUser, related_name='fromFriends')
    toFriend = models.ForeignKey(ProjectUser, related_name='toFriends')
    relationType = models.ForeignKey(RelationType)
    date = models.DateField()

    class Meta:
        unique_together=('fromFriend', 'toFriend')