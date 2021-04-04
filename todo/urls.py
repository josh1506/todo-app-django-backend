from django.urls import path, include
from rest_framework import routers

from .views import TodoView, CheckListView

router = routers.DefaultRouter()
router.register('list', TodoView)
router.register('task', CheckListView)

urlpatterns = [
    path('', include(router.urls))
]
