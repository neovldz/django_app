from rest_framework import viewsets

from models import Tournament, Participant

from .serializers import TournamentSerializer, ParticipantSerializer  # noqa


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
