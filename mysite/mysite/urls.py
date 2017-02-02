from django.conf.urls import include, url
from django.contrib import admin

#Django looks here first when you request a site.
#It tries first to match against these patterns.
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    
]
