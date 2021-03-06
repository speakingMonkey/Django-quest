#encode=utf-8
from django.conf.urls import patterns,include,url
from django.contrib import admin


urlpatterns=patterns('account.views',
        url(r'^register/$','register_user'),
        url(r'^login/$','login_user'),
        url(r'^confirm/(?P<activecode>[\w-]+)/','activate_user'),
        url(r'^logout/$','logout_user'),
        url(r'^userinfo/$','get_userinfo',{"userid":None}),
        url(r'^userinfo/(?P<userid>\d+)[/]{0,1}$','get_userinfo',name='user_detail'),
        url(r'^followuser/$','follow_user'),
        url(r'^upload/image/$','change_image'),
        url(r'searchsuggestions/$','get_suggestions'),
        url(r'','index'),
        )
