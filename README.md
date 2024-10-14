# Email-Sender

A simple program who sends pre-formatted emails, Using pyhton classes.


## Installation
Clone the repo:
   ```bash
   git clone https://github.com/dragnum3xp/project-ject
   ```

Get a Key from the email platform you will use.(This repository uses Gmail)

-https://developers.google.com/gmail/api/guides/sending#python
-https://learn.microsoft.com/en-us/graph/outlook-create-send-messages

Input your key in the variable:
 key = "API_KEY"

 Build your message within the function:

 ```python
 def send_message(self):
        print("New Email")
        self.subject = str(input("Subject: "))
        self.body = str(input("Body of the Email: "))
        sender_email = self.email_address
        receiver_email = input("Enter the email of the receiver: ")
 ```
 Run the code, and create a username and password.
 

       

