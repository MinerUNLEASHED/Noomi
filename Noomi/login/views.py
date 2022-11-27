from django.shortcuts import render


from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
        
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE - PLEASE RECREATE ACCOUNT')
        else:
            print('Someone tried to login and failed.')
            print('Username: {} and password {}'.format(username,password))
            return HttpResponse('invalid login details supplied!')
    else:
        return render(request,'login/HTML.html',{})
    

    
    
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


