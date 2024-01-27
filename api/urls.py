from django.urls import path, include
from rest_framework import routers
from api.views import PeepsView, ActionsPeepView, LoginAPIView, CreateTestUserView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from api.views import EffectViewSet
from mypeeps.settings import LOCUST_TEST

router = routers.DefaultRouter()

router.register('peeps', PeepsView)
#router.register('peeps/effects/<pk:int>', EffectViewSet.as_view({'get':'retrive'}), basename='effects_peeps')

urlpatterns_tests = [
    path('tests/createUser', CreateTestUserView.as_view(), name='create_test_user')
]

urlpatterns = [
    path('', include(router.urls)),
    path('peeps/actions', ActionsPeepView.as_view(), name='actions_peeps'),
    path('peeps/effects/<int:pk>', EffectViewSet.as_view({'get':'retrieve'}), name='effects_peeps'),
    path('login', LoginAPIView.as_view(), name='Login view'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),   
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if LOCUST_TEST == 'True':

    urlpatterns += urlpatterns_tests