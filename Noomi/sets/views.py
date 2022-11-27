from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from sets.models import Sets
from sets.forms import new_set as NewSetForm

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def create_set(request):
    form = NewSetForm()
    if request.method == 'POST':
        form = NewSetForm(request.POST)
    if form.is_valid():
        form.save(commit=False)
        form.user = request.user.username
        form.save(commit=True)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'sets/CREATE_SET.html',{'form':form})
    
    

