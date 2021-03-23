from django.db import models


# Create your models here.
class Key(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Key, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)


class Element(models.Model):
    name = models.CharField(max_length=128)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )


class Attribute(models.Model):
    element = models.ForeignKey(
        Element,
        on_delete=models.CASCADE,
    )
    key = models.ForeignKey(
        Key,
        on_delete=models.CASCADE,
    )
    value = models.CharField(max_length=128, blank=True, null=True)
