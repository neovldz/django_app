from django.contrib.auth.models import User, Group

from rest_framework import serializers

from models import Player, Team, Coach


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ('url', 'name', 'team', 'team_name')


class TeamSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Team
        fields = ('url', 'name', 'coach')


class CoachSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coach
        fields = ('url', 'name')
