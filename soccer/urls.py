from django.conf.urls import url, include

from rest_framework import routers

from soccer import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'coaches', views.CoachViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
