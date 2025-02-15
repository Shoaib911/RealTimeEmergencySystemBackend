import firebase_admin
from firebase_admin import credentials, db, messaging
import os
import json

# Load Firebase credentials from environment variable
# firebase_config_str = os.getenv("FIREBASE_CREDENTIALS")

# if not firebase_config_str:
    # raise ValueError("FIREBASE_CREDENTIALS environment variable is not set.")

# try:
    # firebase_config = json.loads(firebase_config_str)
# except json.JSONDecodeError as e:
    # raise ValueError("Invalid FIREBASE_CREDENTIALS format. Make sure it's a valid JSON string.") from e

def fetch_user_data(user_id):
    ref = db.reference(f"users/{user_id}")
    return ref.get()

def send_alert_to_contacts(alert, contacts):
    for contact in contacts:
        message = messaging.Message(
            notification=messaging.Notification(
                title=f"Emergency Alert: {alert.emergency_type}",
                body=f"User at {alert.location.latitude},{alert.location.longitude}"
            ),
            token=contact["device_token"]
        )
        messaging.send(message)
