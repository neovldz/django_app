from django.db import models


class Tournament(models.Model):
    """
    """

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u"Name: {name}".format(name=self.name)


class Participant(models.Model):
    """
    """

    name = models.CharField(max_length=200)
    tournament = models.ForeignKey(Tournament)

    def __unicode__(self):
        return u"{name} {team}".format(name=self.name, team=self.tournament.name)  # noqa
