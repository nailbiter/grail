from django.db import models

class ActivityType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

# the funniest part of program
class Activity(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# habit of user
class Habit(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

# technical table. Can be used for ordering and distribution of user skills
class SkillType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

# skill of user
class Skill(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    type = models.ForeignKey(SkillType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name