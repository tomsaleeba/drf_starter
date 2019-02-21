from django.conf.urls import url, include
from django.contrib import admin
from dynamic_rest import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from drf_starter.the_app import viewsets

router = routers.DynamicRouter()
router.register_resource(viewsets.UserViewSet)
router.register_resource(viewsets.GroupViewSet)
router.register_resource(viewsets.LocationViewSet)

schema_view = get_schema_view(title='DRF Starter API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='DRF_Starter API', public=False)),
    url(r'^ht/', include('health_check.urls')),
    url(r'^schema/', schema_view),
]
