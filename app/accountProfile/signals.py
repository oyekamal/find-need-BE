from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import Notification
import json


import firebase_admin
from firebase_admin import credentials, messaging

from django.conf import settings

# Access FIREBASE_CREDENTIALS from settings
firebase_credentials = settings.FIREBASE_CREDENTIALS
cred_info = firebase_credentials
# Initialize Firebase only once
cred = credentials.Certificate(cred_info)
firebase_admin.initialize_app(cred)


# Assuming the models are defined in the same file or imported correctly
def send_notification(
    id, token, notification_type, title, body, doc_id, name, is_group, image, member_ids
):
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        data={
            "id": id,
            "notificationType": notification_type,
            "docId": doc_id,
            "name": name,
            "isGroup": str(is_group).lower(),
            "image": image,
            "memberIds": json.dumps(member_ids),
        },
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(aps=messaging.Aps(sound="default")),
            headers={"apns-priority": "10"},
        ),
        token=token,
    )

    try:
        response = messaging.send(message)
        print(f"Successfully sent message: {response}")
        return "Notification sent"
    except Exception as error:
        print(f"Error sending message: {error}")
        return "Error sending notification"


@receiver(post_save, sender=Notification)
def send_notification_on_save(sender, instance, created, **kwargs):
    if created:
        # tokens = instance.get_tokens()
        token = instance.token
        # for token in tokens:
        send_notification(
            id=str(instance.id),
            token=token,
            notification_type=instance.notification_type,
            title=instance.title,
            body=instance.body,
            doc_id=str(instance.doc_id),
            name=instance.name,
            is_group=False,  # Adjust as needed
            image=instance.image,
            member_ids=[],  # Adjust as needed
        )
