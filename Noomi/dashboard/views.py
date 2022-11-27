from django.shortcuts import render
from signup.forms import UserForms
# Create your views here.

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard/HTML.html',{})
    else:
        return HttpResponse(reverse('index'))
