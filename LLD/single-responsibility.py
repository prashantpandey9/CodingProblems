# Class should have one and only one reason to change.
# This means that a class must have only one responsibility

# Code Example:
"""Imagine you have a class called UserManager
that handles user authentication, user profile management, 
and email notifications.
"""

class UserManage:
    def authentication_user(self, username, password):
        self.username = username
        self.password = password
    
    def update_user_profile(self, user_id, new_profile_data):
        # do something
        print(user_id, new_profile_data)
        return {}

    def send_email_notification(self, username, message):
        print(username, message, "Message Sent!")

# here above this class has three responsibility
# Authentication
# Profile Management
# Notification services

# To adhere Single Responsibility Principle we need to separate out the responsibilities to different classes



class UserAuthentication:
    def authentication(self, username, password):
        # define the authentication logic
        pass

class UserManagement:
    def update_user_profile(self, user_id, new_profile_data):
        # add user profile management logic here
        pass

class UserNotification:
    def send_email_notification(self, username, message):
        # add notification logic here
        pass


# Now class has single and well defined responsibility

