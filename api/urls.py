from django.urls import path, include
from rest_framework import routers
from api.views import PeepsView, ActionsPeepView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()

router.register('peeps', PeepsView)

urlpatterns = [
    path('', include(router.urls)),
    path('peeps/actions', ActionsPeepView.as_view(), name="actions_peeps"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),   
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]