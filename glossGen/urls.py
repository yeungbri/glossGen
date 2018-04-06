"""glossGen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from glossGen.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('uploadTarget', uploadTarget),
    path('gloss', gloss),
    path('error', error),
    path('test', test),
    path('', upload),
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^hello/$', hello),
#     url(r'^$', home),
#     url(r'^time/$', curDateTime),
#     url(r'^time/plus/(\d{1,2})/$', hours_ahead),
#     url(r'^timelog/$', timeBase),
#     url(r'^log/$', log),
#     url(r'^notedir/$', notedir),
#     url(r'^note/view/<filename>', viewnote),
# ]
