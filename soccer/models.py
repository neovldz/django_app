from django.db import models

# Create your models here.


class Team(models.Model):
    """"
    my doc string
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

    class Meta:
        verbose_name_plural = "Coaches"

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
