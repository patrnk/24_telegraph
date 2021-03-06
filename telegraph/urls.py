"""telegraph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

import entries.views


urlpatterns = [
    url(r'^$', entries.views.EntryCreateView.as_view(),
        name='create_entry'),
    url(r'^update/(?P<slug>[-\w]+)/$',
        entries.views.EntryUpdateView.as_view(raise_exception=True),
        name='update_entry'),
    url(r'^entry/(?P<slug>[-\w]+)/$', entries.views.EntryDetailView.as_view(),
        name='entry_detail')
]
