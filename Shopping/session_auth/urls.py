from django.urls import path
from .views import RegisterViewSet, SessionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('session', SessionViewSet, basename='session')
router.register('register', RegisterViewSet, basename='register')

urlpatterns = router.urls