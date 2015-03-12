# -*- coding: utf-8 -*-
import requests
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import get_model
from django.forms.models import model_to_dict


Todo = get_model('todo', 'Todo')


def serialize(action, instance):
    return {
        'topic': 'updates',
        'args': [
            action,
            model_to_dict(instance)
        ]
    }


def send(payload):
    requests.post("http://127.0.0.1:8080/notify", json=payload)


@receiver(post_save, sender=Todo, dispatch_uid="server_post_save")
def notify_of_save(sender, instance, created, raw, **kwargs):
    action = 'updated'
    if created:
        action = 'created'
    payload = serialize(action, instance)
    send(payload)


@receiver(post_delete, sender=Todo, dispatch_uid='server_post_delete')
def notify_of_delete(sender, instance, **kwargs):
    payload = serialize('deleted', instance)
    send(payload)
