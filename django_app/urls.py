from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bears', views.BearView)

urlpatterns = [
  path('', include(router.urls))
]