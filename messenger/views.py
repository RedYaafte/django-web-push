from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Profile


class WebPushView(TemplateView):
    template_name = 'messenger/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Lests go!!'})


def onesignal_register(request):
    '''Receives the onesignal playerid of this user'''
    profile = Profile.objects.get(
        user=request.user)  # The model where you will to save the profile.
    if request.POST.get('playerId'):
        profile.onesignal_playerId = request.POST.get('playerId')
        profile.save()
        return HttpResponse('Done')
    return HttpResponse('Something went wrong')
