from ast import Try
import asyncio
import json
from celery import shared_task,Celery,states
from healthApp import settings
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import medicine_notifications
from celery.exceptions import Ignore


@shared_task(bind=True)
def broadcast_notification(self,data):
    print(data)
    try:
        notification=medicine_notifications.objects.filter(id=int(data))
        if len(notification)>0:
            notification=notification.first()
            channel_layer=get_channel_layer()
            loop=asyncio.new_event_loop()
            loop.run_until_complete(channel_layer.group_send(
                "notification_broadcast",
                {
                    'type': 'send_notification',
                    'message': json.dumps(notification.message)
                }
            ))
            notification.sent=True
            notification.save()
            return "Done"
        else:
            self.update_state(
                state='FAILURE',
                meta={'exe':'Not Found'}
            )
            raise Ignore()
    except:
        self.update_state(
            state='FAILURE',
            meta={'exe': 'Failed'}
        )
        raise Ignore()

