from django.shortcuts import render, get_object_or_404
from django.core import serializers

from .models import ProfileName, ProjectUser

def profile_by_id(request, profileId):
    """
    get request on url .../profile/profileID
    and return html view, based on object
    of class Project User, where user_id = profileId
    """
    user = get_object_or_404(ProjectUser, user_id=profileId)
    return render(request, 'userprofile/userProfile.html', {'user': user})

def profile_by_name(request, profileName):
    """
    get request on url .../profile/profileName
    and return html view, based on object user
    of class Project User, where profileName=profileName.name
    and user = profileName.user
    """
    profile = get_object_or_404(ProfileName, name=profileName)
    user = profile.user
    return render(request, 'userprofile/userProfile.html', {'user': user})

def profile_by_id_api(request, profileId):
    """
    get request on url .../profile/profileID
    and return JSON, with all information about object user
    of class Project User, where user_id = profileId
    """
    user = get_object_or_404(ProjectUser, user_id=profileId)
    return serializers.serialize("json", user)

def profile_by_name_api(request, profileName):
    """
    get request on url .../profile/profileName
    and return JSON, with user object
    of class Project User, where profileName=profileName.name
    and user = profileName.user
    """
    profile = get_object_or_404(ProfileName, name=profileName)
    user = profile.user
    return serializers.serialize("json", user)