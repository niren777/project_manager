from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Projects(models.Model):
    name = models.CharField(_('project name'), max_length=60)
    description = models.CharField(_('description'), max_length=200)
    start_date = models.DateTimeField(_('start date'))
    end_date = models.DateTimeField(_('end date'))

class Tasks(models.Model):
    name = models.CharField(_('task name'), max_length=60)
    description = models.CharField(_('description'), max_length=200)
    project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )