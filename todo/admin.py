# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import get_model


Todo = get_model('todo', 'Todo')
admin.site.register(Todo)
