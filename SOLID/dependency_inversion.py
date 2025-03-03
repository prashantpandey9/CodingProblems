"""High-level modules should not depend on low-level modules; both should depend on abstractions.

This means that a particular class should not depend directly on another class, but on an abstraction (interface) of this class.
"""
# Here the EmailService depends on the GmalClient

class GmailClient:
    def send_email(self, recipient, subject, body):
        #logic to send email
        pass

class EmailService:
    def __init__(self):
        self.email_client = GmailClient()
    
    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)

# Improved code

class EmailClient:
    def send_email(self, recipient, subject, body):
        return NotImplementedError


class GmailClient(EmailClient):
    def send_email(self, recipient, subject, body):
        #logic to send email
        pass

class OutLookClient(EmailClient):
    def send_email(self, recipient, subject, body):
        #logic to send email
        pass

class EmailService:
    def __init__(self, email_client):
        self.email_client = email_client
    
    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)



# usage
gmail_client = GmailClient()
email_service = EmailService(gmail_client)
email_service.send_email("recipient@example.com", "Subject", "EMail Body")