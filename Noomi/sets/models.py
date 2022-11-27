from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your models here.
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class Sets(models.Model):
    created_by= models.CharField(max_length=100,blank=False,null=False)  # type: ignore
    
    title = models.CharField(max_length=100,blank=False,null=True)
    
    # User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User,null=True)  # type: ignore
    
    term1key = models.CharField(max_length=100,blank=False)
    term1value = models.CharField(max_length=100,blank=False)
    
    term2key = models.CharField(max_length=100,blank=False)
    term2value = models.CharField(max_length=100,blank=False)

    term3key = models.CharField(max_length=100,blank=False)
    term3value = models.CharField(max_length=100,blank=False)

    term4key = models.CharField(max_length=100,blank=True)
    term4value = models.CharField(max_length=100,blank=True)

    term5key = models.CharField(max_length=100,blank=True)
    term5value = models.CharField(max_length=100,blank=True)

    term6key = models.CharField(max_length=100,blank=True)
    term6value = models.CharField(max_length=100,blank=True)
    
    term7key = models.CharField(max_length=100,blank=True)
    term7value = models.CharField(max_length=100,blank=True)

    term8key = models.CharField(max_length=100,blank=True)
    term8value = models.CharField(max_length=100,blank=True)

    term9key = models.CharField(max_length=100,blank=True)
    term9value = models.CharField(max_length=100,blank=True)

    term10key = models.CharField(max_length=100,blank=True)
    term10value = models.CharField(max_length=100,blank=True)

    term11key = models.CharField(max_length=100,blank=True)
    term11value = models.CharField(max_length=100,blank=True)
    
    term12key = models.CharField(max_length=100,blank=True)
    term12value = models.CharField(max_length=100,blank=True)

    term13key = models.CharField(max_length=100,blank=True)
    term13value = models.CharField(max_length=100,blank=True)

    term14key = models.CharField(max_length=100,blank=True)
    term14value = models.CharField(max_length=100,blank=True)

    term15key = models.CharField(max_length=100,blank=True)
    term15value = models.CharField(max_length=100,blank=True)

    term16key = models.CharField(max_length=100,blank=True)
    term16value = models.CharField(max_length=100,blank=True)
    
    term17key = models.CharField(max_length=100,blank=True)
    term17value = models.CharField(max_length=100,blank=True)

    term18key = models.CharField(max_length=100,blank=True)
    term18value = models.CharField(max_length=100,blank=True)

    term19key = models.CharField(max_length=100,blank=True)
    term19value = models.CharField(max_length=100,blank=True)

    term20key = models.CharField(max_length=100,blank=True)
    term20value = models.CharField(max_length=100,blank=True)

    term21key = models.CharField(max_length=100,blank=True)
    term21value = models.CharField(max_length=100,blank=True)
    
    term22key = models.CharField(max_length=100,blank=True)
    term22value = models.CharField(max_length=100,blank=True)

    term23key = models.CharField(max_length=100,blank=True)
    term23value = models.CharField(max_length=100,blank=True)

    term24key = models.CharField(max_length=100,blank=True)
    term24value = models.CharField(max_length=100,blank=True)

    term25key = models.CharField(max_length=100,blank=True)
    term25value = models.CharField(max_length=100,blank=True)

    term26key = models.CharField(max_length=100,blank=True)
    term26value = models.CharField(max_length=100,blank=True)
    
    term27key = models.CharField(max_length=100,blank=True)
    term27value = models.CharField(max_length=100,blank=True)

    term28key = models.CharField(max_length=100,blank=True)
    term28value = models.CharField(max_length=100,blank=True)

    term29key = models.CharField(max_length=100,blank=True)
    term29value = models.CharField(max_length=100,blank=True)

    term30key = models.CharField(max_length=100,blank=True)
    term30value = models.CharField(max_length=100,blank=True)

    term31key = models.CharField(max_length=100,blank=True)
    term31value = models.CharField(max_length=100,blank=True)
    
    term32key = models.CharField(max_length=100,blank=True)
    term32value = models.CharField(max_length=100,blank=True)

    term33key = models.CharField(max_length=100,blank=True)
    term33value = models.CharField(max_length=100,blank=True)

    term34key = models.CharField(max_length=100,blank=True)
    term34value = models.CharField(max_length=100,blank=True)

    term35key = models.CharField(max_length=100,blank=True)
    term35value = models.CharField(max_length=100,blank=True)

    term36key = models.CharField(max_length=100,blank=True)
    term36value = models.CharField(max_length=100,blank=True)
    
    term37key = models.CharField(max_length=100,blank=True)
    term37value = models.CharField(max_length=100,blank=True)

    term38key = models.CharField(max_length=100,blank=True)
    term38value = models.CharField(max_length=100,blank=True)

    term39key = models.CharField(max_length=100,blank=True)
    term39value = models.CharField(max_length=100,blank=True)

    term40key = models.CharField(max_length=100,blank=True)
    term40value = models.CharField(max_length=100,blank=True)

    term41key = models.CharField(max_length=100,blank=True)
    term41value = models.CharField(max_length=100,blank=True)
    
    term42key = models.CharField(max_length=100,blank=True)
    term42value = models.CharField(max_length=100,blank=True)

    term43key = models.CharField(max_length=100,blank=True)
    term43value = models.CharField(max_length=100,blank=True)

    term44key = models.CharField(max_length=100,blank=True)
    term44value = models.CharField(max_length=100,blank=True)

    term45key = models.CharField(max_length=100,blank=True)
    term45value = models.CharField(max_length=100,blank=True)

    term46key = models.CharField(max_length=100,blank=True)
    term46value = models.CharField(max_length=100,blank=True)
    
    term47key = models.CharField(max_length=100,blank=True)
    term47value = models.CharField(max_length=100,blank=True)

    term48key = models.CharField(max_length=100,blank=True)
    term48value = models.CharField(max_length=100,blank=True)

    term49key = models.CharField(max_length=100,blank=True)
    term49value = models.CharField(max_length=100,blank=True)

    term50key = models.CharField(max_length=100,blank=True)
    term50value = models.CharField(max_length=100,blank=True)

    term51key = models.CharField(max_length=100,blank=True)
    term51value = models.CharField(max_length=100,blank=True)
    
    term52key = models.CharField(max_length=100,blank=True)
    term52value = models.CharField(max_length=100,blank=True)

    term53key = models.CharField(max_length=100,blank=True)
    term53value = models.CharField(max_length=100,blank=True)

    term54key = models.CharField(max_length=100,blank=True)
    term54value = models.CharField(max_length=100,blank=True)

    term55key = models.CharField(max_length=100,blank=True)
    term55value = models.CharField(max_length=100,blank=True)

    term56key = models.CharField(max_length=100,blank=True)
    term56value = models.CharField(max_length=100,blank=True)
    
    term57key = models.CharField(max_length=100,blank=True)
    term57value = models.CharField(max_length=100,blank=True)

    term58key = models.CharField(max_length=100,blank=True)
    term58value = models.CharField(max_length=100,blank=True)

    term59key = models.CharField(max_length=100,blank=True)
    term59value = models.CharField(max_length=100,blank=True)

    term60key = models.CharField(max_length=100,blank=True)
    term60value = models.CharField(max_length=100,blank=True)

    term61key = models.CharField(max_length=100,blank=True)
    term61value = models.CharField(max_length=100,blank=True)
    
    term62key = models.CharField(max_length=100,blank=True)
    term62value = models.CharField(max_length=100,blank=True)

    term63key = models.CharField(max_length=100,blank=True)
    term63value = models.CharField(max_length=100,blank=True)

    term64key = models.CharField(max_length=100,blank=True)
    term64value = models.CharField(max_length=100,blank=True)

    term65key = models.CharField(max_length=100,blank=True)
    term65value = models.CharField(max_length=100,blank=True)

    term66key = models.CharField(max_length=100,blank=True)
    term66value = models.CharField(max_length=100,blank=True)
    
    term67key = models.CharField(max_length=100,blank=True)
    term67value = models.CharField(max_length=100,blank=True)

    term68key = models.CharField(max_length=100,blank=True)
    term68value = models.CharField(max_length=100,blank=True)

    term69key = models.CharField(max_length=100,blank=True)
    term69value = models.CharField(max_length=100,blank=True)

    term70key = models.CharField(max_length=100,blank=True)
    term70value = models.CharField(max_length=100,blank=True)

    term71key = models.CharField(max_length=100,blank=True)
    term71value = models.CharField(max_length=100,blank=True)
    
    term72key = models.CharField(max_length=100,blank=True)
    term72value = models.CharField(max_length=100,blank=True)

    term73key = models.CharField(max_length=100,blank=True)
    term73value = models.CharField(max_length=100,blank=True)

    term74key = models.CharField(max_length=100,blank=True)
    term74value = models.CharField(max_length=100,blank=True)

    term75key = models.CharField(max_length=100,blank=True)
    term75value = models.CharField(max_length=100,blank=True)

    term76key = models.CharField(max_length=100,blank=True)
    term76value = models.CharField(max_length=100,blank=True)
    
    term77key = models.CharField(max_length=100,blank=True)
    term77value = models.CharField(max_length=100,blank=True)

    term78key = models.CharField(max_length=100,blank=True)
    term78value = models.CharField(max_length=100,blank=True)

    term79key = models.CharField(max_length=100,blank=True)
    term79value = models.CharField(max_length=100,blank=True)

    term80key = models.CharField(max_length=100,blank=True)
    term80value = models.CharField(max_length=100,blank=True)

    term81key = models.CharField(max_length=100,blank=True)
    term81value = models.CharField(max_length=100,blank=True)
    
    term82key = models.CharField(max_length=100,blank=True)
    term82value = models.CharField(max_length=100,blank=True)

    term83key = models.CharField(max_length=100,blank=True)
    term83value = models.CharField(max_length=100,blank=True)

    term84key = models.CharField(max_length=100,blank=True)
    term84value = models.CharField(max_length=100,blank=True)

    term85key = models.CharField(max_length=100,blank=True)
    term85value = models.CharField(max_length=100,blank=True)

    term86key = models.CharField(max_length=100,blank=True)
    term86value = models.CharField(max_length=100,blank=True)
    
    term87key = models.CharField(max_length=100,blank=True)
    term87value = models.CharField(max_length=100,blank=True)

    term88key = models.CharField(max_length=100,blank=True)
    term88value = models.CharField(max_length=100,blank=True)

    term89key = models.CharField(max_length=100,blank=True)
    term89value = models.CharField(max_length=100,blank=True)

    term90key = models.CharField(max_length=100,blank=True)
    term90value = models.CharField(max_length=100,blank=True)

    term91key = models.CharField(max_length=100,blank=True)
    term91value = models.CharField(max_length=100,blank=True)
    
    term92key = models.CharField(max_length=100,blank=True)
    term92value = models.CharField(max_length=100,blank=True)

    term93key = models.CharField(max_length=100,blank=True)
    term93value = models.CharField(max_length=100,blank=True)

    term94key = models.CharField(max_length=100,blank=True)
    term94value = models.CharField(max_length=100,blank=True)

    term95key = models.CharField(max_length=100,blank=True)
    term95value = models.CharField(max_length=100,blank=True)

    term96key = models.CharField(max_length=100,blank=True)
    term96value = models.CharField(max_length=100,blank=True)
    
    term97key = models.CharField(max_length=100,blank=True)
    term97value = models.CharField(max_length=100,blank=True)

    term98key = models.CharField(max_length=100,blank=True)
    term98value = models.CharField(max_length=100,blank=True)

    term99key = models.CharField(max_length=100,blank=True)
    term99value = models.CharField(max_length=100,blank=True)

    term100key = models.CharField(max_length=100,blank=True)
    term100value = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.user

    
# class SetCount(models.Model):
#     created_by= models.CharField(max_length=100)
