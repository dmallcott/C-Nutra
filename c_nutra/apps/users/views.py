from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

#Import a user registration form
from apps.users.forms import UserRegisterForm
from apps.users.models import UserProfile, UserProfileForm

from django.contrib.auth.middleware import get_user



# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# User Register View
def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponse('User created succcessfully.')
        else:
            form = UserRegisterForm()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        #Pass the context to a template
        return render_to_response('registration/register.html', context)
    else:
        return HttpResponseRedirect('/')

# 
@login_required
def user_profile(request):
    if request.method == 'POST':
        user = get_user(request)
        form = UserProfileForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data.get('height', 'default1')
            UserProfile.objects.filter(user=user).update(height=height)
            return HttpResponseRedirect('/')

    else:
        profile = request.user.get_profile()
        edited_profile = UserProfileForm
        user = get_user(request)
        #user = request.POSt['user']
        #context = {'user': user}
        return render_to_response('profile/profile.html',{'profile':profile, 'edited_profile':edited_profile}, context_instance=RequestContext(request))