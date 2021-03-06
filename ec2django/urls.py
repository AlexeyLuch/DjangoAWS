""" ec2django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^', include('helloworld.urls')),
  url('qwe/', include('poll.urls')),
  url('jet/', include('jet.urls', 'jet')),
   url('accounts/', include('allauth.urls')),
   url('chat_channel/', include('chat_channel.urls')),
   # path('ref_pages/', include('ref_pages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
