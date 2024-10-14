import smtplib
import ssl
from email.message import EmailMessage
import csv as c

class User():
    def __init__(self, username, password, email_address):
        self.username = username
        self.password = password
        self.email_address = email_address

    #Method to verify a user
    def login(self):
        self.username = input("Username: ")
        self.password = input("Password: ")

        try:
            with open("users.csv", "r") as users:
                csv_reader = c.reader(users)

                for row in csv_reader:
                    username = row[0].strip()
                    password = row[1].strip()

                    if self.username == username and self.password == password:
                        print("Login successful!")
                        self.email_address = row[2].strip()
                        return
                print("Invalid username or password.")

        except FileNotFoundError as fe:
            print(f"We can't find the file {fe}")

    #Method to store a new user
    def new_user(self):
        self.username = input("Create a Username: ")
        self.password = input("Create a Password: ")
        self.email_address = input("Input your email address: ")

        with open("users.csv", "a") as n_user:
            n_user.write(f"{self.username}, {self.password}, {self.email_address}\n")

class Email(User):
    def __init__(self, email_address, username, subject, body):
        super().__init__(username, "", email_address)
        self.subject = subject
        self.body = body

    def send_message(self):
        print("New Email")
        self.subject = str(input("Subject: "))
        self.body = str(input("Body of the Email: "))
        sender_email = self.email_address
        receiver_email = input("Enter the email of the receiver: ")

        message = EmailMessage()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = self.subject

        html = f"""
            <html>
                <body>
                    <h1>{self.subject}</h1>
                    <p>{self.body}</p>
                </body>
            </html>
            """

        message.add_alternative(html, subtype="html")

        key = "API_KEY"
        context = ssl.create_default_context()

        print("Sending Email!")

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, key)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")

        except PermissionError as pe:
            print(f"Seems that you don't have all the permissions: {pe}")

# Create an instance of the User Email class
new_user = User(username="", password="", email_address="")
user_email = Email(email_address="", username="", subject="", body="")

# Calling the login method or creating a user
print("Please Select")
print()
choice = input(" 1 - Login \n2 - Create a User")
if choice == "1":
    user_email.login()
elif choice == "2":
    user_email.new_user()

user_email.send_message()
    

# Use the send_message method to send an email using the logged-in user information


