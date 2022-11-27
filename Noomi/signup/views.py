from django.shortcuts import render
from signup.forms import UserForms
# Create your views here.

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout



def signup(request):
    registered = False
        
    if request.method == 'POST':
        user_form = UserForms(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #Hashes password
            user.save()
        
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForms()
        
    return render(request,'signup/HTML.html',{'user_form':user_form,'registered':registered})