from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.urls import path
##############################

from django.contrib import admin
admin.autodiscover()

import anestforthree.views

# Examples:
# url(r'^$', 'core.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', anestforthree.views.index, name='index'),
    path('admin/', admin.site.urls),
]
