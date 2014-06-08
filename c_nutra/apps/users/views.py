from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Import a user registration form
from apps.users.forms import UserRegisterForm
from apps.users.models import UserProfile,
from apps.users.forms import UserProfileForm, UserForm
from django.contrib.auth.models import User

from django.contrib.auth.middleware import get_user
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import get_messages

# This will be deprecated for django-registration - 06/06/2014
# User Register View


def user_register(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponse('User created succcessfully.')
                # no good. fix this
        else:
            form = UserRegisterForm()
        context = {}
        context.update(csrf(request))
        context['form'] = form
        # Pass the context to a template
        return render_to_response('registration/register.html', context)
    else:
        return HttpResponseRedirect('/')

# User Profile View
@login_required
def user_profile(request):
    if request.method == 'POST':
        user = get_user(request)
        # The user-form atribute in the request represents changes were made to the user information
        if "user-form" in request.POST:
            form = UserForm(request.POST)
            # The form is evaluated and if valid its updated
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                if username:
                    User.objects.filter(id=user.id).update(username=username)
                if email:
                    User.objects.filter(id=user.id).update(email=email)
                if first_name:
                    User.objects.filter(id=user.id).update(
                        first_name=first_name)
                if last_name:
                    User.objects.filter(id=user.id).update(last_name=last_name)
                # A message is added so the user knows his information was updated
                messages.add_message(
                    request, messages.SUCCESS,
                    'Perfil actualizado correctamente.',
                    extra_tags={'user': 'user'})
            # If there is an error with the inputs a message is added with the errors
            else:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, messages.ERROR, error)
        # The profile-form atribute in the request represents changes were made to the user profile
        elif "profile-form" in request.POST:
            form = UserProfileForm(request.POST)
            # The form is evaluated and if valid its updated
            if form.is_valid():
                birthday = form.cleaned_data.get('birthday')
                gender = form.cleaned_data.get('gender')
                height = form.cleaned_data.get('height')
                weight = form.cleaned_data.get('weight')
                elbow_diameter = form.cleaned_data.get('elbow_diameter')
                if birthday:
                    UserProfile.objects.filter(
                        user=user).update(birthday=birthday)
                if gender:
                    UserProfile.objects.filter(user=user).update(gender=gender)
                if height:
                    UserProfile.objects.filter(user=user).update(height=height)
                if weight:
                    UserProfile.objects.filter(user=user).update(weight=weight)
                if elbow_diameter:
                    UserProfile.objects.filter(user=user).update(
                        elbow_diameter=elbow_diameter)
                # A message is added so the user knows his profile was updated
                messages.add_message(
                    request, messages.SUCCESS,
                    'Perfil actualizado correctamente.',
                    extra_tags=('profile'))
            # If there is an error with the inputs a message is added with the errors
            else:
                for field in form:
                    for error in field.errors:
                        messages.add_message(
                            request, messages.ERROR,
                            error,
                            extra_tags=('profile'))
        # User is redirected to the profile page
        return HttpResponseRedirect('/accounts/profile/')
    else:
        # The user profile is obtained and two empy forms for user information and profile are created
        profile = request.user.get_profile()
        form_user = UserForm
        form_profile = UserProfileForm
        # Possible previous messages are collected, processed and added to the context 
        messages_temp = get_messages(request)
        profile_messages = False
        for message in messages_temp:
            if 'profile' in message.tags:
                profile_messages = True
        return render(
            request,
            'profile/profile.html',
            {
                'profile': profile,
                'form_profile': form_profile,
                'form_user': form_user,
                'profile_messages': profile_messages
            }
        )
