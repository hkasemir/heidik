from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^', include('mainpage.urls')),
]
