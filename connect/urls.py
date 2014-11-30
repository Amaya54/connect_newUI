from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'connect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'register.views.register', name='register'),
    url(r'^login/', 'login.views.login', name='login'),
    url(r'^fetchPost/', 'posting.views.fetchPost', name='fetchPost'),
    url(r'^post/', 'posting.views.post', name='post'),        
    
)
