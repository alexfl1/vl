from __future__ import unicode_literals

from django.db import models


from django.utils import timezone

# Create your models here.
from nodes.models import nodes


class domains(models.Model):
#    author = models.ForeignKey('auth.User')
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(
 #           default=timezone.now)
#    published_date = models.DateTimeField(
#            blank=True, null=True)
#    node_id = models.IntegerField()
    name = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)
    node_id = models.ForeignKey(nodes,default=0)
    description = models.TextField()
