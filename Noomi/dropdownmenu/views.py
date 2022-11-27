from django.shortcuts import render
from django.http import HttpResponse

def about(request):
     my_dict = {"variable name":"variable meaning"}
     return render(request,'dropdownmenu/ABOUT.html',context=my_dict)


def help(request):
     my_dict = {"variable name":"variable meaning"}
     return render(request,'dropdownmenu/HELP.html',context=my_dict)
