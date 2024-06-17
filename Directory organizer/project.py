import smtplib
import ssl
from email.message import EmailMessage
import csv as c
from typing import Optional, Tuple, Union
import customtkinter as ctk
from customtkinter import CTkFont

ctk.set_default_color_theme("dark-blue")




# Create an instance of the User Email class


# Calling the login method
#user_email.login()

# Use the send_message method to send an email using the logged-in user information
#user_email.send_message()




class User:
    def __init__(self, username, password, email_address):
        self.username = username
        self.password = password
        self.email_address = email_address


    def login(self):
        try:
            with open("users.csv", "r") as users:
                csv_reader = c.reader(users)

                for row in csv_reader:
                    stored_username = row[0].strip()
                    stored_password = row[1].strip()

                    if self.username == stored_username and self.password == stored_password:
                        self.email_address = row[2].strip()
                        return True
                return False

        except FileNotFoundError as fe:
            print(f"We can't find the file {fe}")
            return False

    def new_user(self):
        self.username = input("Create a Username: ")
        self.password = input("Create a Password: ")
        self.email_address = input("Input your email address: ")

        with open("users.csv", "a") as n_user:
            n_user.write(f"{self.username}, {self.password}, {self.email_address}\n")


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

        key = "plsv tdgj clud kvxr"
        context = ssl.create_default_context()

        print("Sending Email!")

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, key)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")

        except PermissionError as pe:
            print(f"Seems that you don't have all the permissions: {pe}")


class Loginwindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Email Sender")
        self.exist_user = User(username="", password="", email_address="")
        self.new_user = User(username="", password="", email_address="")
        self.user_email = Email(email_address="", username="", subject="", body="")
        self._create_login_screen()

    def _create_login_screen(self):
        self.geometry("500x350")
        display_frame = ctk.CTkFrame(master=self, height=400, width=250)
        display_frame.pack(ipadx=50, ipady=10, padx=20, pady=10, fill="both")

        self.login_text = ctk.CTkLabel(
            master=display_frame, text="Login", font=ctk.CTkFont(size=28, weight="bold"),
        )
        self.login_text.pack(pady=20, padx=60, fill="none", expand=True)

        self.user_field = ctk.CTkLabel(
            master=display_frame, text="Username", font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.user_field.pack(pady=10, side=ctk.TOP, fill="none", expand=False)

        self.user_input = ctk.CTkEntry(
            master=display_frame, text_color="black", placeholder_text="Username", placeholder_text_color="gray"
        )
        self.user_input.pack(fill="none", expand=False)

        self.pass_field = ctk.CTkLabel(
            master=display_frame, text="Password", font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.pass_field.pack(pady=10, side=ctk.TOP, fill="none", expand=False)

        self.pass_input = ctk.CTkEntry(
            master=display_frame, text_color="black", placeholder_text="Password", placeholder_text_color="gray"
        )
        self.pass_input.pack(fill="none", expand=False)

        self.login_bttn = ctk.CTkButton(
            master=display_frame, fg_color="gray", border_color="black", text="Login", hover_color="darkgray",
        )
        self.login_bttn.pack(pady=5, side=ctk.TOP, fill="none", expand=False)
        self.login_bttn.bind("<Button-1>", self.login_logic)

        self.new_button = ctk.CTkButton(
            master=display_frame, fg_color="gray", border_color="black", text="New User", hover_color="darkgray", command=self.create_user
        )
        self.new_button.pack(pady=5, side=ctk.TOP, fill="none", expand=False)

        self.create_user_window = None

    def login_logic(self, event):
        self.exist_user.username = self.user_input.get()
        self.exist_user.password = self.pass_input.get()

        # Validate the username and password
        if not self.exist_user.username or not self.exist_user.password:
            print("Please enter both username and password.")
            return

        # Call the login method of the User class
        if self.exist_user.login():
            print("Login successful!")
            # Here you can proceed to the next screen or perform other actions
        else:
            print("Invalid username or password.")

    def create_user(self):
        if self.create_user_window is None or not self.create_user_window.winfo_exists():
            self.create_user_window = Registerwindow(self)  # create window if it's None or destroyed
        else:
            self.create_user_window.focus()


class Registerwindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("New User")
        self.master = master
        self.new_user = User(username="", password="", email_address="")
        self._create_register_screen()

    def _create_register_screen(self):
        display_frame = ctk.CTkFrame(master=self, height=400, width=250)
        display_frame.pack(ipadx=50, ipady=10, padx=20, pady=10, fill="both")

        self.login_text = ctk.CTkLabel(
            master=display_frame, text="Register", font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.login_text.pack(pady=20, padx=60, fill="none", expand=True)

        self.create_user = ctk.CTkEntry(
            master=display_frame, text_color="black", placeholder_text="Create Username", placeholder_text_color="gray"
        )
        self.create_user.pack(fill="none", expand=False)

        self.create_pass = ctk.CTkEntry(
            master=display_frame, text_color="black", placeholder_text="Create Password", placeholder_text_color="gray"
        )
        self.create_pass.pack(fill="none", expand=False)

        self.add_email = ctk.CTkEntry(
            master=display_frame, text_color="black", placeholder_text="Email Addres", placeholder_text_color="gray"
        )
        self.add_email.pack(fill="none", expand=False)

        self.add_bttn = ctk.CTkButton(
            master=display_frame, fg_color="gray", border_color="black", text="Create User", hover_color="darkgray",
        )
        self.add_bttn.pack(pady=5, side=ctk.TOP, fill="none", expand=False)
        self.add_bttn.bind("<Button-1>", self.add_logic)
        
        self.focus_force()

    def add_logic(self, event):
        self.new_user.username = self.create_user.get()
        self.new_user.password = self.create_pass.get()
        self.new_user.email_address = self.add_email.get()

        with open("users.csv", "a") as n_user:
            n_user.write(f"{self.new_user.username}, {self.new_user.password}, {self.new_user.email_address}\n")

        self.destroy()




screen = Loginwindow()
screen.mainloop()


