from django.contrib import admin

from .projectUser.models import ProjectUser, UserM2MUser, UserM2MAchievement, AchievementOwnType, RelationType
from .projectUser.gifts import Gift
from .projectUser.achievements import Achievement, AchievementType
from .hero.models import HeroClass, Hero, Ability
from .hero.equipment import Equipment, EquipmentType
from .training.models import Skill, SkillType, Habit, ActivityType, Activity

admin.site.register(ProjectUser)
admin.site.register(AchievementType)
admin.site.register(Achievement)
admin.site.register(Gift)
admin.site.register(HeroClass)
admin.site.register(EquipmentType)
admin.site.register(Equipment)
admin.site.register(Ability)
admin.site.register(Hero)
admin.site.register(SkillType)
admin.site.register(Skill)
admin.site.register(Habit)
admin.site.register(ActivityType)
admin.site.register(Activity)

admin.site.register(UserM2MUser)
admin.site.register(AchievementOwnType)
admin.site.register(RelationType)
admin.site.register(UserM2MAchievement)