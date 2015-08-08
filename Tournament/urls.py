from django.conf.urls import url, include

from rest_framework import routers

from Tournament import views

router = routers.DefaultRouter()
router.register(r'tournaments', views.TournamentViewSet)
router.register(r'participants', views.ParticipantViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
