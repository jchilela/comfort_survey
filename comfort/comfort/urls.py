from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from comfortapp.views import TaskViewSet


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, 'task')


urlpatterns = [
    # Examples:
    url(r'^task', include(router.urls)),
    url(r'^$', 'comfortapp.views.home', name='home'),
    url(r'^strategies', 'comfortapp.views.strategies', name='strategies'),

    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
]
