from django.db import models
from django.utils.translation import ugettext_lazy as _


class Todo(models.Model):
    message = models.TextField(_("message"))

    def __unicode__(self):
        return self.message
