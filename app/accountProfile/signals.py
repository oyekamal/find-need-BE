from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import Notification
import json


import firebase_admin
from firebase_admin import credentials, messaging

cred_info = {
    "type": "service_account",
    "project_id": "findneed-a8392",
    "private_key_id": "9ac40056410a5317fd429e60d5ef9b30f11f9da2",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDU13Y9erbsB1TY\ncarlN+VaItLCM2PFixR0XrnN3yKWSU34+QVkTfg8otlJqI1Ashk+cuWFxNdvV1R/\nXZO69/z70uEjPZi8xi9wr88m/39gjkzdarRWomyyk03u7zEDgeyHvW1LxX7MEjJD\nqNjsgr/ufg0Qi7voa/zVhtJRxOMlrEMPRASNfcYmIj3dy0mrCOfBtF6mkycHoHUQ\n7PLcOYPjt4HKofIeVXgNmJbJfLn78ax3cTti6etRKG2OV4oGn7dQIZhF+pXtfDLC\nJ0xCW16fH7LqT+ZuDS+4bhwKZ5OeQ0NcIzgFvro1fsrVu6ucI0FNMI2MMSPlIa9R\nLleBTXfLAgMBAAECggEAGbTyW4eUS1qxVTkZXnkLUwEsunbxgH0FWe7M+0ANkeBF\nsiIFlDFUn6I9o0df1CYOpXvEHA2DxbdjBcUcIDNuk03LknGQnpBDT5V0bC3kyRk2\n0HFgWaxhe4oOGiM6pMVO97AZ4NJ4N5alCoX8uUgrfVctJcfyyKYuUe3oPicNFlII\n/2FqaRwHW4Piw7ugrUB2u1uPI6OSKK4p1AcIqcVzaiSfHclzNKvwwCf6bPfvPAek\nRaClDP53p84AeseyKHUBcCYNWkMOlUuv5GI067HpRi+Fjwr09OPYl/+46UEPBi77\ne3cKmWNgjadTLy3p026UypsLjqnLwEL0zjCZ5GN+WQKBgQD5QCehmVbWqwPbcgBh\naAPAfiX9U7wt64k5iN618ZxDXwG6X9UECx44ONJDM+sKp/yNSCSWDz3M0FlhZ6XW\ntWhyqftWbVPMvYl9I5qQTkXfVzhLSaZ3bhc3N2CNc8x67k0lmR4Puq554aeXb/Bo\njK+G6kviIGFeMSsjhFfbXxyP0wKBgQDamuoR2zf7BoTyYsn458vLypr2DmXp0fgz\nU6JjgZ0RcTDUlUuUd/zPgXBsrt1ftD4TIPmJzLXRGdP4aeTynvna1qVgOJiHOzoA\nHa5wwyw32e7RvQI+YRKogxzTO+/nPtBmjFywGRBqNXnNruIDnHLESv+CBGNNIbEC\nbKgrR6V1KQKBgDBBS2rt1PIaidSibZBuIsvRoGk7HOOHBjotVXDEJgylCCCdDRCL\nVn5sAckg9BBMFYkEvpCOwtg0Phmth13aIS6R2icRY3fv+f5QNkxZ2w0yRaPNznyw\nw63c+sRn9t6V5DmzOy6wZbcTCO84rMKQ+iqUkbxlqHQj8MYfiSLfdxghAoGAaKyn\nChfTLWMIw9tj5MhxQErqeomYaSa+Vy1j44vLvu9ZN2GpiBUQO/g58gClRc9Tresr\nMb2RDef1JMzn8PkIoK4JEBLpjk9gzW9o+Nurz66N+WYsrdvjiEcHxWm8zRi5x3DM\nbRIDVyf2A/QKizodhjp3MDWTqvpH/OY0fEzZQEkCgYEAh4+KYGWUnc2jDnHZ41JA\nqTSkRGPlqc+b01bBUmWaj1a954cwe+R10hb0F8l9SZrJlziwGZs7z5bGmPm3bQQE\nLKw1nth2QPNbHOXS9cY0uKqPU68FQieOw/Vkgh9rEyIJbKZz4aGRpV8OPRc+zBSC\nfISaw19g8kMGt1NCuuhV6+Y=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-zoozm@findneed-a8392.iam.gserviceaccount.com",
    "client_id": "106224707926934177634",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zoozm%40findneed-a8392.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com",
}
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
            id=instance.id,
            token=token,
            notification_type=instance.notification_type,
            title=instance.title,
            body=instance.body,
            doc_id=instance.doc_id,
            name=instance.name,
            is_group=False,  # Adjust as needed
            image=instance.image,
            member_ids=[],  # Adjust as needed
        )
