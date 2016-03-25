from django.template import loader
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from main.projectUser.achievements import AchievementType

def index(request):
    return HttpResponse('Hey, man')

def achievements(request):
    achievementTypesList = AchievementType.objects.order_by('id')[:5]
    template = loader.get_template(('data/index.html'))
    context = {
        'achievementTypesList': achievementTypesList,
    }
    return HttpResponse(template.render(context, request))

def achievementType(request, achievementTypeName):
    achievementType = get_object_or_404(AchievementType, name=achievementTypeName)
    return render(request, 'data/achievementType.html', {'achievementType': achievementType})

def achievement(request, achievementType_id, achievement_id):
    return HttpResponse('here is information about achievements of type %s' % achievementType_id + 'achievement number %s' %achievement_id)

def offerAchievement(request, achievementType_id):
    return HttpResponse('you are offering us a new achievement of type %s' % achievementType_id)