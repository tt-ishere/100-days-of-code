from twilio.rest import Client
from environment_variables import account_sid, auth_token


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, sms):
        message = self.client.messages.create(
            body=sms,
            from_="+17407167716",
            to="+233268125555",
        )
        print(message.sid)
