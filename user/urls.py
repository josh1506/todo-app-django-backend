from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from .views import UserView, FacebookLoginView

router = routers.DefaultRouter()
router.register('account', UserView)

urlpatterns = [
    path('facebook/auth/', FacebookLoginView.as_view()),
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
]
