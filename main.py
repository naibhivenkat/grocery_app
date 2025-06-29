from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login_screen import LoginScreen
from customer_screen import CustomerScreen
from shop_screen import ShopScreen

class GroceryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(CustomerScreen(name="customer"))
        sm.add_widget(ShopScreen(name="shop"))
        return sm

if __name__ == "__main__":
    GroceryApp().run()
