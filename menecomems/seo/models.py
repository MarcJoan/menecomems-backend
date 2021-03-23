from django.db import models


# Create your models here.
class Robot(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class URL(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class UserAgent(models.Model):
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.value


class Rule(models.Model):
    robot = models.ForeignKey(
        Robot,
        on_delete=models.CASCADE
    )
    agent = models.ForeignKey(
        UserAgent,
        on_delete=models.CASCADE
    )
    url = models.ForeignKey(
        URL,
        on_delete=models.CASCADE
    )
    allowed = models.BooleanField(default=True)

    class Meta:
        unique_together = ('robot', 'agent', 'url', 'allowed',)

    def __str__(self):
        return self.robot.name + " - " + self.agent.name + ": " + self.url.name
