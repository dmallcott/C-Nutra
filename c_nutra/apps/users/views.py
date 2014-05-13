from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from models import UserForm
from models import UserProfileForm

def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return django.http.HttpResponseRedirect('/')
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render_to_response('registration/register.html', 
                                               dict(userform=uf,
                                                    userprofileform=upf),
                                               context_instance=RequestContext(request))