from rest_framework import serializers

from models import Tournament, Participant


class TournamentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tournament
        fields = ('url', 'name')


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Participant
        fields = ('url', 'name', 'tournament')
