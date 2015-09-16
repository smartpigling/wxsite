# -*-coding:utf-8 -*-
"""
Created on 2015-09-10
@author: 汤晓川

"""

from django.conf.urls import patterns,url
from .views import Weixin, UserLocationFetching

urlpatterns = patterns('',
    url(r'^location/fetch/$', UserLocationFetching.as_view(), name='weixin_fetch_user_location'),
    url(r'^(\w+)/$', Weixin.as_view(), name='weixin_entry'),
)
