from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     my_dict = {"variable name":"variable meaning"}
     return render(request,'homepage/HTML.html',context=my_dict)
