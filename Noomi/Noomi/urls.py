"""Noomi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from homepage import views as homepage_views
from signup import views as signup_views
from login import views as login_views
from dropdownmenu import views as ddm_views
from dashboard import views as dashboard_views
from sets import views as sets_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage_views.index, name='index'),
    # url(r'^signup/', signup_views.signup, name='signup'),
    # url(r'^login/', login_views.user_login, name='user_login'),
    # url(r'^logout/$',login_views.user_logout,name='user_logout'),
    url(r'^about/$',ddm_views.about,name='about'),
    url(r'^help/$',ddm_views.help,name='help'),
    # url(r'^dashboard/$',dashboard_views.dashboard,name='dashboard'),
    url(r'^set/$',sets_views.create_set,name='create_set'),
]



from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
