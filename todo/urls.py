from django.urls import path, include
from rest_framework import routers

from .views import TodoView

router = routers.DefaultRouter()
router.register('list', TodoView)

urlpatterns = [
    path('', include(router.urls))
]
