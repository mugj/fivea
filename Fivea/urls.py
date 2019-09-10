"""Fivea URL Configuration

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
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from Fivea.settings import MEDIA_ROOT#, STATIC_ROOT
from django.views.static import serve
from provinces.views import ProvincesListView, IndexDataView
from scenerys.views import SceneryListView, SceneryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexDataView.as_view(), name="index"),
    url('^province/$', ProvincesListView.as_view(), name="provincesList"),
    url('^province/(?P<provinces_id>\d+)/$', SceneryListView.as_view(), name="sceneryList"),
    url('^scenery/(?P<scenery_id>\d+)/$', SceneryView.as_view(), name="scenery"),
    url('^contact/$', TemplateView.as_view(template_name='contact.html'), name="contact"),


    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


