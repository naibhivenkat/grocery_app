# from kivy.uix.screenmanager import Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from utils import load_users
#
# class LoginScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.users = load_users()
#
#         layout = BoxLayout(orientation="vertical")
#         self.username_input = TextInput(hint_text="Username")
#         self.password_input = TextInput(hint_text="Password", password=True)
#         login_button = Button(text="Login")
#         login_button.bind(on_press=self.login)
#
#         self.message = Label()
#
#         layout.add_widget(self.username_input)
#         layout.add_widget(self.password_input)
#         layout.add_widget(login_button)
#         layout.add_widget(self.message)
#
#         self.add_widget(layout)
#
#     def login(self, instance):
#         username = self.username_input.text
#         password = self.password_input.text
#         for user in self.users:
#             if user["username"] == username and user["password"] == password:
#                 self.manager.current = user["role"]
#                 self.manager.get_screen(user["role"]).set_user(username)
#                 return
#         self.message.text = "Invalid credentials"


from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from utils import load_users

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.users = load_users()

        layout = BoxLayout(orientation="vertical")

        self.role_spinner = Spinner(
            text="Select Role",
            values=("customer", "shop"),
            size_hint=(1, 0.2)
        )

        self.username_input = TextInput(hint_text="Username")
        self.password_input = TextInput(hint_text="Password", password=True)
        login_button = Button(text="Login")
        login_button.bind(on_press=self.login)

        self.message = Label()

        layout.add_widget(self.role_spinner)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(self.message)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        role = self.role_spinner.text

        if role not in ["customer", "shop"]:
            self.message.text = "Please select a role"
            return

        for user in self.users:
            if user["username"] == username and user["password"] == password and user["role"] == role:
                self.manager.current = role
                self.manager.get_screen(role).set_user(username)
                return

        self.message.text = "Invalid credentials or role mismatch"
