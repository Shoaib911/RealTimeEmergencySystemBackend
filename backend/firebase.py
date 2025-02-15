import firebase_admin
from firebase_admin import credentials, db, messaging


cred = credentials.Certificate("C:\\Users\\sufik\\OneDrive\\Documents\\GitHub\\RealTimeEmergencySystem\\backend\\elisasentry-firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://elisasentry-default-rtdb.asia-southeast1.firebasedatabase.app"
})

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
