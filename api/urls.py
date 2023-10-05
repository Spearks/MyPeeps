from django.urls import path, include
from rest_framework import routers
from api.views import PeepsView, ActionsPeepView, LoginAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register('peeps', PeepsView)


urlpatterns = [
    path('', include(router.urls)),
    path('peeps/actions', ActionsPeepView.as_view(), name='actions_peeps'),
    path('login', LoginAPIView.as_view(), name='Login view'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),   
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]