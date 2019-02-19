from django.conf.urls import url, include
from django.contrib import admin
from dynamic_rest import routers
from rest_framework.documentation import include_docs_urls

from drf_starter.the_app import viewsets

router = routers.DynamicRouter()
router.register_resource(viewsets.UserViewSet)
router.register_resource(viewsets.GroupViewSet)
router.register_resource(viewsets.LocationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='DRF_Starter API', public=False))
]
