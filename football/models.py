from django.db import models


class Team(models.Model):
    """
    """

    name = models.CharField(max_length=200)
    coach = models.ForeignKey('Coach', null=True, blank=True)

    def __unicode__(self):
        return u"Name: {name}".format(name=self.name)


class Player(models.Model):
    """
    """

    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u"{name} {team}".format(name=self.name, team=self.team.name)


class Coach(models.Model):
    """
    """

    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Coaches"

    def __unicode__(self):
        return self.name
