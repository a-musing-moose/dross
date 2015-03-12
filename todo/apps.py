# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TodoConfig(AppConfig):
    name = 'todo'
    verbose_name = _("Todos")
    label = 'todo'

    def ready(self):
        from . import handlers
