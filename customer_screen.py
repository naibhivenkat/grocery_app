# # # from kivy.uix.screenmanager import Screen
# # # from kivy.uix.boxlayout import BoxLayout
# # # from kivy.uix.label import Label
# # # from kivy.uix.image import Image
# # # from kivy.uix.button import Button
# # # from kivy.uix.scrollview import ScrollView
# # # from kivy.uix.popup import Popup
# # # from utils import load_items, place_order
# # #
# # # class CustomerScreen(Screen):
# # #     def __init__(self, **kwargs):
# # #         super().__init__(**kwargs)
# # #         self.cart = {}
# # #         self.username = ""
# # #
# # #     def set_user(self, username):
# # #         self.username = username
# # #         self.display_items()
# # #
# # #     def display_items(self):
# # #         self.clear_widgets()
# # #         layout = BoxLayout(orientation="vertical")
# # #
# # #         scroll = ScrollView()
# # #         items_layout = BoxLayout(orientation="vertical", size_hint_y=None)
# # #         items_layout.bind(minimum_height=items_layout.setter('height'))
# # #
# # #         for item in load_items():
# # #             box = BoxLayout(size_hint_y=None, height=150)
# # #
# # #             if "image" in item:
# # #                 img = Image(source=f"assets/{item['image']}", size_hint_x=0.3)
# # #                 box.add_widget(img)
# # #
# # #             info = f"{item['name']} - ₹{item['price']}"
# # #             box.add_widget(Label(text=info))
# # #
# # #             add_btn = Button(text="Add to Cart")
# # #             add_btn.bind(on_press=lambda inst, name=item["name"]: self.add_to_cart(name))
# # #             box.add_widget(add_btn)
# # #             items_layout.add_widget(box)
# # #
# # #         scroll.add_widget(items_layout)
# # #         layout.add_widget(scroll)
# # #
# # #         btns = BoxLayout(size_hint_y=0.2)
# # #
# # #         cart_btn = Button(text="View Cart")
# # #         cart_btn.bind(on_press=self.view_cart)
# # #
# # #         logout_btn = Button(text="Logout")
# # #         logout_btn.bind(on_press=lambda x: self.logout())
# # #
# # #         btns.add_widget(cart_btn)
# # #         btns.add_widget(logout_btn)
# # #         layout.add_widget(btns)
# # #
# # #         self.add_widget(layout)
# # #
# # #     def add_to_cart(self, item_name):
# # #         self.cart[item_name] = self.cart.get(item_name, 0) + 1
# # #
# # #     def view_cart(self, instance):
# # #         content = BoxLayout(orientation="vertical", spacing=10, padding=10)
# # #         total = 0
# # #
# # #         for item, qty in self.cart.items():
# # #             item_total = self.get_price(item) * qty
# # #             total += item_total
# # #             content.add_widget(Label(text=f"{item} x {qty} = ₹{item_total}"))
# # #
# # #         content.add_widget(Label(text=f"Total: ₹{total}", bold=True))
# # #
# # #         btns = BoxLayout(size_hint_y=0.2)
# # #
# # #         place_btn = Button(text="Place Order")
# # #         place_btn.bind(on_press=lambda x: self.place_order(popup))
# # #
# # #         cancel_btn = Button(text="Cancel Order")
# # #         cancel_btn.bind(on_press=lambda x: self.cancel_order(popup))
# # #
# # #         btns.add_widget(place_btn)
# # #         btns.add_widget(cancel_btn)
# # #
# # #         content.add_widget(btns)
# # #
# # #         popup = Popup(title="Cart", content=content, size_hint=(0.85, 0.8))
# # #         popup.open()
# # #
# # #     def get_price(self, name):
# # #         for item in load_items():
# # #             if item["name"] == name:
# # #                 return item["price"]
# # #         return 0
# # #
# # #     def place_order(self, popup):
# # #         order = place_order(self.username, self.cart)
# # #         self.cart = {}
# # #         popup.dismiss()
# # #         self.show_message("Order placed!")
# # #
# # #     def cancel_order(self, popup):
# # #         self.cart = {}
# # #         popup.dismiss()
# # #         self.show_message("Cart cleared.")
# # #
# # #     def logout(self):
# # #         self.manager.current = "login"
# # #
# # #     def show_message(self, msg):
# # #         popup = Popup(title="Info", content=Label(text=msg), size_hint=(0.6, 0.4))
# # #         popup.open()
# #
# # # from kivy.uix.screenmanager import Screen
# # # from kivy.uix.boxlayout import BoxLayout
# # # from kivy.uix.label import Label
# # # from kivy.uix.image import Image
# # # from kivy.uix.button import Button
# # # from kivy.uix.scrollview import ScrollView
# # # from kivy.uix.popup import Popup
# # # from kivy.uix.spinner import Spinner
# # # from utils import load_items, place_order
# # #
# # # class CustomerScreen(Screen):
# # #     def __init__(self, **kwargs):
# # #         super().__init__(**kwargs)
# # #         self.cart = {}
# # #         self.username = ""
# # #         self.selected_shop = ""
# # #         self.available_shops = ["shop1", "shop2"]  # Update as needed
# # #
# # #     def set_user(self, username):
# # #         self.username = username
# # #         self.cart = {}
# # #         self.select_shop()
# # #
# # #     def select_shop(self):
# # #         self.clear_widgets()
# # #         layout = BoxLayout(orientation="vertical")
# # #         layout.add_widget(Label(text="Select Shop"))
# # #
# # #         spinner = Spinner(
# # #             text="Select",
# # #             values=self.available_shops,
# # #             size_hint=(1, 0.2)
# # #         )
# # #         layout.add_widget(spinner)
# # #
# # #         btn = Button(text="Continue")
# # #         btn.bind(on_press=lambda x: self.set_shop(spinner.text))
# # #         layout.add_widget(btn)
# # #
# # #         self.add_widget(layout)
# # #
# # #     def set_shop(self, shop_name):
# # #         if shop_name == "Select":
# # #             return
# # #         self.selected_shop = shop_name
# # #         self.display_items()
# # #
# # #     def display_items(self):
# # #         self.clear_widgets()
# # #         layout = BoxLayout(orientation="vertical")
# # #
# # #         scroll = ScrollView()
# # #         items_layout = BoxLayout(orientation="vertical", size_hint_y=None)
# # #         items_layout.bind(minimum_height=items_layout.setter('height'))
# # #
# # #         for item in load_items():
# # #             if item.get("shop") != self.selected_shop:
# # #                 continue
# # #
# # #             box = BoxLayout(size_hint_y=None, height=150)
# # #
# # #             if "image" in item:
# # #                 img = Image(source=f"assets/{item['image']}", size_hint_x=0.3)
# # #                 box.add_widget(img)
# # #
# # #             info = f"{item['name']} - ₹{item['price']}"
# # #             box.add_widget(Label(text=info))
# # #
# # #             add_btn = Button(text="Add to Cart")
# # #             add_btn.bind(on_press=lambda inst, name=item["name"]: self.add_to_cart(name))
# # #             box.add_widget(add_btn)
# # #             items_layout.add_widget(box)
# # #
# # #         scroll.add_widget(items_layout)
# # #         layout.add_widget(scroll)
# # #
# # #         btns = BoxLayout(size_hint_y=0.2)
# # #
# # #         cart_btn = Button(text="View Cart")
# # #         cart_btn.bind(on_press=self.view_cart)
# # #
# # #         logout_btn = Button(text="Logout")
# # #         logout_btn.bind(on_press=lambda x: self.logout())
# # #
# # #         btns.add_widget(cart_btn)
# # #         btns.add_widget(logout_btn)
# # #         layout.add_widget(btns)
# # #
# # #         self.add_widget(layout)
# # #
# # #     def add_to_cart(self, item_name):
# # #         self.cart[item_name] = self.cart.get(item_name, 0) + 1
# # #
# # #     def view_cart(self, instance):
# # #         content = BoxLayout(orientation="vertical", spacing=10, padding=10)
# # #         content.add_widget(Label(text=f"Shop: {self.selected_shop}"))
# # #         total = 0
# # #         detailed_cart = []
# # #
# # #         for item, qty in self.cart.items():
# # #             price = self.get_price(item)
# # #             item_total = price * qty
# # #             total += item_total
# # #             content.add_widget(Label(text=f"{item} x {qty} = ₹{item_total}"))
# # #             detailed_cart.append({"name": item, "qty": qty, "price": price})
# # #
# # #         content.add_widget(Label(text=f"Total: ₹{total}", bold=True))
# # #
# # #         btns = BoxLayout(size_hint_y=0.2)
# # #
# # #         place_btn = Button(text="Place Order")
# # #         place_btn.bind(on_press=lambda x: self.place_order(popup, detailed_cart))
# # #
# # #         cancel_btn = Button(text="Cancel Order")
# # #         cancel_btn.bind(on_press=lambda x: self.cancel_order(popup))
# # #
# # #         btns.add_widget(place_btn)
# # #         btns.add_widget(cancel_btn)
# # #
# # #         content.add_widget(btns)
# # #
# # #         popup = Popup(title="Cart", content=content, size_hint=(0.85, 0.8))
# # #         popup.open()
# # #
# # #     def get_price(self, name):
# # #         for item in load_items():
# # #             if item["name"] == name:
# # #                 return item["price"]
# # #         return 0
# # #
# # #     def place_order(self, popup, detailed_cart):
# # #         order = place_order(self.username, detailed_cart, self.selected_shop)
# # #         self.cart = {}
# # #         popup.dismiss()
# # #         self.show_message("Order placed!")
# # #
# # #     def cancel_order(self, popup):
# # #         self.cart = {}
# # #         popup.dismiss()
# # #         self.show_message("Cart cleared.")
# # #
# # #     def logout(self):
# # #         self.manager.current = "login"
# # #
# # #     def show_message(self, msg):
# # #         popup = Popup(title="Info", content=Label(text=msg), size_hint=(0.6, 0.4))
# # #         popup.open()
# #
# #
# # from kivy.uix.screenmanager import Screen
# # from kivy.uix.boxlayout import BoxLayout
# # from kivy.uix.label import Label
# # from kivy.uix.image import Image
# # from kivy.uix.button import Button
# # from kivy.uix.scrollview import ScrollView
# # from kivy.uix.popup import Popup
# # from kivy.uix.spinner import Spinner
# # from utils import load_items, place_order
# # import os
# #
# # class CustomerScreen(Screen):
# #     def __init__(self, **kwargs):
# #         super().__init__(**kwargs)
# #         self.cart = {}
# #         self.username = ""
# #         self.selected_shop = ""
# #         self.available_shops = ["shop1", "shop2"]  # Update as needed
# #
# #     def set_user(self, username):
# #         self.username = username
# #         self.cart = {}
# #         self.select_shop()
# #
# #     def select_shop(self):
# #         self.clear_widgets()
# #         layout = BoxLayout(orientation="vertical")
# #         layout.add_widget(Label(text="Select Shop"))
# #
# #         spinner = Spinner(
# #             text="Select",
# #             values=self.available_shops,
# #             size_hint=(1, 0.2)
# #         )
# #         layout.add_widget(spinner)
# #
# #         btn = Button(text="Continue")
# #         btn.bind(on_press=lambda x: self.set_shop(spinner.text))
# #         layout.add_widget(btn)
# #
# #         self.add_widget(layout)
# #
# #     def set_shop(self, shop_name):
# #         if shop_name == "Select":
# #             return
# #         self.selected_shop = shop_name
# #         self.display_items()
# #
# #     def display_items(self):
# #         self.clear_widgets()
# #         layout = BoxLayout(orientation="vertical")
# #
# #         scroll = ScrollView()
# #         items_layout = BoxLayout(orientation="vertical", size_hint_y=None)
# #         items_layout.bind(minimum_height=items_layout.setter('height'))
# #
# #         for item in load_items():
# #             if item.get("shop") != self.selected_shop:
# #                 continue
# #
# #             box = BoxLayout(size_hint_y=None, height=150)
# #
# #             if "image" in item:
# #                 image_path = os.path.join(os.getcwd(), "assets", item["image"])
# #                 img = Image(source=image_path, size_hint_x=0.3)
# #                 box.add_widget(img)
# #
# #             info = f"{item['name']} - ₹{item['price']}"
# #             box.add_widget(Label(text=info))
# #
# #             add_btn = Button(text="Add to Cart")
# #             add_btn.bind(on_press=lambda inst, name=item["name"]: self.add_to_cart(name))
# #             box.add_widget(add_btn)
# #             items_layout.add_widget(box)
# #
# #         scroll.add_widget(items_layout)
# #         layout.add_widget(scroll)
# #
# #         btns = BoxLayout(size_hint_y=0.2)
# #
# #         cart_btn = Button(text="View Cart")
# #         cart_btn.bind(on_press=self.view_cart)
# #
# #         logout_btn = Button(text="Logout")
# #         logout_btn.bind(on_press=lambda x: self.logout())
# #
# #         btns.add_widget(cart_btn)
# #         btns.add_widget(logout_btn)
# #         layout.add_widget(btns)
# #
# #         self.add_widget(layout)
# #
# #     def add_to_cart(self, item_name):
# #         self.cart[item_name] = self.cart.get(item_name, 0) + 1
# #
# #     def view_cart(self, instance):
# #         content = BoxLayout(orientation="vertical", spacing=10, padding=10)
# #         content.add_widget(Label(text=f"Shop: {self.selected_shop}"))
# #         total = 0
# #         detailed_cart = []
# #
# #         for item, qty in self.cart.items():
# #             price = self.get_price(item)
# #             item_total = price * qty
# #             total += item_total
# #             content.add_widget(Label(text=f"{item} x {qty} = ₹{item_total}"))
# #             detailed_cart.append({"name": item, "qty": qty, "price": price})
# #
# #         content.add_widget(Label(text=f"Total: ₹{total}", bold=True))
# #
# #         btns = BoxLayout(size_hint_y=0.2)
# #
# #         place_btn = Button(text="Place Order")
# #         place_btn.bind(on_press=lambda x: self.place_order(popup, detailed_cart))
# #
# #         cancel_btn = Button(text="Cancel Order")
# #         cancel_btn.bind(on_press=lambda x: self.cancel_order(popup))
# #
# #         btns.add_widget(place_btn)
# #         btns.add_widget(cancel_btn)
# #
# #         content.add_widget(btns)
# #
# #         popup = Popup(title="Cart", content=content, size_hint=(0.85, 0.8))
# #         popup.open()
# #
# #     def get_price(self, name):
# #         for item in load_items():
# #             if item["name"] == name:
# #                 return item["price"]
# #         return 0
# #
# #     def place_order(self, popup, detailed_cart):
# #         order = place_order(self.username, detailed_cart, self.selected_shop)
# #         self.cart = {}
# #         popup.dismiss()
# #         self.show_message("Order placed!")
# #
# #     def cancel_order(self, popup):
# #         self.cart = {}
# #         popup.dismiss()
# #         self.show_message("Cart cleared.")
# #
# #     def logout(self):
# #         self.manager.current = "login"
# #
# #     def show_message(self, msg):
# #         popup = Popup(title="Info", content=Label(text=msg), size_hint=(0.6, 0.4))
# #         popup.open()
#
#
# from kivy.uix.screenmanager import Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.popup import Popup
# from kivy.uix.spinner import Spinner
# from datetime import datetime
# from utils import load_items, place_order
# from bill_generator import generate_pdf_bill
# import os
#
# class CustomerScreen(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cart = {}
#         self.username = ""
#         self.selected_shop = ""
#         self.payment_method = ""
#         self.cart_popup = None
#         self.available_shops = ["shop1", "shop2"]
#
#     def set_user(self, username):
#         self.username = username
#         self.cart = {}
#         self.select_shop()
#
#     def select_shop(self):
#         self.clear_widgets()
#         layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
#         layout.add_widget(Label(text="Select Shop", font_size=20))
#         spinner = Spinner(text="Select", values=self.available_shops, size_hint=(1, 0.2))
#         layout.add_widget(spinner)
#         btn = Button(text="Continue", font_size=18)
#         btn.bind(on_press=lambda x: self.set_shop(spinner.text))
#         layout.add_widget(btn)
#         self.add_widget(layout)
#
#     def set_shop(self, shop_name):
#         if shop_name == "Select":
#             return
#         self.selected_shop = shop_name
#         self.display_items()
#
#     def display_items(self):
#         self.clear_widgets()
#         layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
#         scroll = ScrollView()
#         items_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=10)
#         items_layout.bind(minimum_height=items_layout.setter('height'))
#
#         for item in load_items():
#             if item.get("shop") != self.selected_shop:
#                 continue
#
#             box = BoxLayout(size_hint_y=None, height=140, spacing=10)
#             if "image" in item:
#                 path = os.path.join("assets", item["image"])
#                 box.add_widget(Image(source=path, size_hint_x=0.3))
#             info = f"{item['name']} - ₹{item['price']}"
#             box.add_widget(Label(text=info, font_size=18))
#             add_btn = Button(text="Add to Cart", size_hint_x=0.3)
#             add_btn.bind(on_press=lambda inst, name=item["name"]: self.add_to_cart(name))
#             box.add_widget(add_btn)
#             items_layout.add_widget(box)
#
#         scroll.add_widget(items_layout)
#         layout.add_widget(scroll)
#
#         btns = BoxLayout(size_hint_y=0.15, spacing=10)
#         cart_icon = Image(source="assets/cart.png", size_hint_x=0.2)
#         btns.add_widget(cart_icon)
#         cart_btn = Button(text="View Cart", font_size=16)
#         cart_btn.bind(on_press=self.view_cart)
#         logout_btn = Button(text="Logout", font_size=16)
#         logout_btn.bind(on_press=lambda x: self.logout())
#         btns.add_widget(cart_btn)
#         btns.add_widget(logout_btn)
#         layout.add_widget(btns)
#         self.add_widget(layout)
#
#     def add_to_cart(self, item):
#         self.cart[item] = self.cart.get(item, 0) + 1
#
#     def remove_from_cart(self, item):
#         if item in self.cart:
#             self.cart[item] -= 1
#             if self.cart[item] <= 0:
#                 del self.cart[item]
#
#     def get_price(self, name):
#         for item in load_items():
#             if item["name"] == name:
#                 return item["price"]
#         return 0
#
#     def get_item_image(self, name):
#         for item in load_items():
#             if item["name"] == name and "image" in item:
#                 return os.path.join("assets", item["image"])
#         return None
#
#     def change_qty(self, item, delta):
#         if delta > 0:
#             self.add_to_cart(item)
#         else:
#             self.remove_from_cart(item)
#         self.cart_popup.dismiss()
#         self.view_cart(None)
#
#     def view_cart(self, instance):
#         if not self.cart:
#             self.show_message("Your cart is empty.")
#             return
#
#         content = BoxLayout(orientation="vertical", spacing=10, padding=10)
#         close_btn = Button(text="❌", size_hint_y=None, height=40, background_color=(1, 0, 0, 1))
#         close_btn.bind(on_press=lambda x: self.cart_popup.dismiss())
#         content.add_widget(close_btn)
#         content.add_widget(Label(text=f"Shop: {self.selected_shop}", font_size=18))
#         total = 0
#         detailed_cart = []
#
#         for item, qty in self.cart.items():
#             price = self.get_price(item)
#             total += price * qty
#             row = BoxLayout(size_hint_y=None, height=40)
#             logo = self.get_item_image(item)
#             if logo:
#                 row.add_widget(Image(source=logo, size_hint_x=0.2))
#             row.add_widget(Label(text=f"{item} x {qty} = ₹{price * qty}", font_size=16))
#             plus = Button(text="+", size_hint_x=0.1)
#             plus.bind(on_press=lambda x, name=item: self.change_qty(name, 1))
#             minus = Button(text="-", size_hint_x=0.1)
#             minus.bind(on_press=lambda x, name=item: self.change_qty(name, -1))
#             row.add_widget(plus)
#             row.add_widget(minus)
#             content.add_widget(row)
#             detailed_cart.append({"name": item, "qty": qty, "price": price})
#
#         content.add_widget(Label(text=f"Total: ₹{total}", font_size=18))
#         pay_box = BoxLayout(size_hint_y=0.2, spacing=5)
#         for method in ["UPI", "Card", "Cash"]:
#             b = Button(text=method)
#             b.bind(on_press=lambda x, m=method: self.set_payment_and_confirm(detailed_cart, m))
#             pay_box.add_widget(b)
#         content.add_widget(pay_box)
#
#         back_btn = Button(text="Back to Items")
#         back_btn.bind(on_press=lambda x: (self.cart_popup.dismiss(), self.display_items()))
#         content.add_widget(back_btn)
#
#         self.cart_popup = Popup(title="Your Cart", content=content, size_hint=(0.95, 0.95))
#         self.cart_popup.open()
#
#     def set_payment_and_confirm(self, detailed_cart, method):
#         self.payment_method = method
#         now = datetime.now()
#         date_str = now.strftime("%Y-%m-%d")
#         time_str = now.strftime("%H:%M:%S")
#         total = sum(i["qty"] * i["price"] for i in detailed_cart)
#
#         box = BoxLayout(orientation="vertical", spacing=10, padding=10)
#         close_btn = Button(text="❌", size_hint_y=None, height=40, background_color=(1, 0, 0, 1))
#         box.add_widget(close_btn)
#         box.add_widget(Label(text=f"Shop: {self.selected_shop}", font_size=18))
#         box.add_widget(Label(text=f"Customer: {self.username}", font_size=16))
#         box.add_widget(Label(text=f"Date: {date_str}  Time: {time_str}", font_size=14))
#         box.add_widget(Label(text=f"Payment Mode: {method}", font_size=16))
#         for item in detailed_cart:
#             box.add_widget(Label(text=f"{item['name']} x {item['qty']} @ ₹{item['price']}", font_size=14))
#         box.add_widget(Label(text=f"Total: ₹{total}", font_size=18))
#         confirm = Button(text="Confirm Order", font_size=16)
#         back = Button(text="Back to Cart", font_size=16)
#
#         popup = Popup(title="Confirm Order", content=box, size_hint=(0.9, 0.9))
#         close_btn.bind(on_press=popup.dismiss)
#         confirm.bind(on_press=lambda x: self.place_order_and_close(popup))
#         back.bind(on_press=popup.dismiss)
#         box.add_widget(confirm)
#         box.add_widget(back)
#         popup.open()
#
#     def place_order_and_close(self, confirm_popup):
#         order = place_order(self.username,
#             [{"name": k, "qty": v, "price": self.get_price(k)} for k, v in self.cart.items()],
#             self.selected_shop
#         )
#         order["payment"] = self.payment_method
#         generate_pdf_bill(order)
#         self.cart = {}
#         confirm_popup.dismiss()
#         if self.cart_popup:
#             self.cart_popup.dismiss()
#         self.show_message("Order placed! PDF generated.")
#
#     def logout(self):
#         self.manager.current = "login"
#
#     def show_message(self, msg):
#         content = BoxLayout(orientation="vertical", spacing=10)
#         label = Label(text=msg, font_size=16)
#         close_btn = Button(text="Close", size_hint_y=None, height=40)
#         popup = Popup(title="Info", content=content, size_hint=(0.6, 0.4))
#         close_btn.bind(on_press=popup.dismiss)
#         content.add_widget(label)
#         content.add_widget(close_btn)
#         popup.open()


from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from datetime import datetime
from utils import load_items, place_order
from bill_generator import generate_pdf_bill
import os

class CustomerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cart = {}
        self.username = ""
        self.selected_shop = ""
        self.payment_method = ""
        self.cart_popup = None
        self.available_shops = ["shop1", "shop2"]

    def set_user(self, username):
        self.username = username
        self.cart = {}
        self.select_shop()

    def select_shop(self):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        layout.add_widget(Label(text="Select Shop", font_size=28))
        spinner = Spinner(text="Select", values=self.available_shops, size_hint=(1, 0.2), font_size=22)
        layout.add_widget(spinner)
        btn = Button(text="Continue", font_size=24, size_hint_y=0.2)
        btn.bind(on_press=lambda x: self.set_shop(spinner.text))
        layout.add_widget(btn)
        self.add_widget(layout)

    def set_shop(self, shop_name):
        if shop_name == "Select":
            return
        self.selected_shop = shop_name
        self.display_items()

    def display_items(self):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        scroll = ScrollView()
        items_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=20)
        items_layout.bind(minimum_height=items_layout.setter('height'))

        for item in load_items():
            if item.get("shop") != self.selected_shop:
                continue
            box = BoxLayout(size_hint_y=None, height=160, spacing=10)
            if "image" in item:
                path = os.path.join("assets", item["image"])
                box.add_widget(Image(source=path, size_hint_x=0.3))
            info = f"{item['name']} - Rs. {item['price']}"
            box.add_widget(Label(text=info, font_size=22))
            add_btn = Button(text="Add to Cart", size_hint_x=0.3, font_size=20)
            add_btn.bind(on_press=lambda inst, name=item["name"]: self.add_to_cart(name))
            box.add_widget(add_btn)
            items_layout.add_widget(box)

        scroll.add_widget(items_layout)
        layout.add_widget(scroll)

        btns = BoxLayout(size_hint_y=0.15, spacing=10)
        cart_icon = Image(source="assets/cart.png", size_hint_x=0.2)
        btns.add_widget(cart_icon)
        cart_btn = Button(text="View Cart", font_size=20)
        cart_btn.bind(on_press=self.view_cart)
        logout_btn = Button(text="Logout", font_size=20)
        logout_btn.bind(on_press=lambda x: self.logout())
        btns.add_widget(cart_btn)
        btns.add_widget(logout_btn)
        layout.add_widget(btns)
        self.add_widget(layout)

    def add_to_cart(self, item):
        self.cart[item] = self.cart.get(item, 0) + 1

    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart[item] -= 1
            if self.cart[item] <= 0:
                del self.cart[item]

    def get_price(self, name):
        for item in load_items():
            if item["name"] == name:
                return item["price"]
        return 0

    def get_item_image(self, name):
        for item in load_items():
            if item["name"] == name and "image" in item:
                return os.path.join("assets", item["image"])
        return None

    def change_qty(self, item, delta):
        if delta > 0:
            self.add_to_cart(item)
        else:
            self.remove_from_cart(item)
        self.cart_popup.dismiss()
        self.view_cart(None)

    def view_cart(self, instance):
        if not self.cart:
            self.show_message("Your cart is empty.")
            return
        content = BoxLayout(orientation="vertical", spacing=12, padding=10)
        close_btn = Button(text="❌", size_hint_y=None, height=40, background_color=(1, 0, 0, 1), font_size=20)
        close_btn.bind(on_press=lambda x: self.cart_popup.dismiss())
        content.add_widget(close_btn)
        content.add_widget(Label(text=f"Shop: {self.selected_shop}", font_size=24))
        total = 0
        detailed_cart = []

        for item, qty in self.cart.items():
            price = self.get_price(item)
            total += price * qty
            row = BoxLayout(size_hint_y=None, height=60, spacing=10)
            logo = self.get_item_image(item)
            if logo:
                row.add_widget(Image(source=logo, size_hint_x=0.2))
            row.add_widget(Label(text=f"{item} x {qty} = Rs. {price * qty}", font_size=20))
            plus = Button(text="+", size_hint_x=0.1, font_size=20)
            plus.bind(on_press=lambda x, name=item: self.change_qty(name, 1))
            minus = Button(text="-", size_hint_x=0.1, font_size=20)
            minus.bind(on_press=lambda x, name=item: self.change_qty(name, -1))
            row.add_widget(plus)
            row.add_widget(minus)
            content.add_widget(row)
            detailed_cart.append({"name": item, "qty": qty, "price": price})

        content.add_widget(Label(text=f"Total: Rs. {total}", font_size=24))
        pay_box = BoxLayout(size_hint_y=0.2, spacing=10)
        for method in ["UPI", "Card", "Cash"]:
            b = Button(text=method, font_size=20)
            b.bind(on_press=lambda x, m=method: self.set_payment_and_confirm(detailed_cart, m))
            pay_box.add_widget(b)
        content.add_widget(pay_box)

        back_btn = Button(text="Back to Items", font_size=20)
        back_btn.bind(on_press=lambda x: (self.cart_popup.dismiss(), self.display_items()))
        content.add_widget(back_btn)

        self.cart_popup = Popup(title="Your Cart", content=content, size_hint=(0.95, 0.95))
        self.cart_popup.open()

    def set_payment_and_confirm(self, detailed_cart, method):
        self.payment_method = method
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        total = sum(i["qty"] * i["price"] for i in detailed_cart)

        box = BoxLayout(orientation="vertical", spacing=10, padding=10)
        close_btn = Button(text="❌", size_hint_y=None, height=40, background_color=(1, 0, 0, 1), font_size=20)
        box.add_widget(close_btn)
        box.add_widget(Label(text=f"Shop: {self.selected_shop}", font_size=22))
        box.add_widget(Label(text=f"Customer: {self.username}", font_size=20))
        box.add_widget(Label(text=f"Date: {date_str}  Time: {time_str}", font_size=18))
        box.add_widget(Label(text=f"Payment Mode: {method}", font_size=20))
        for item in detailed_cart:
            box.add_widget(Label(text=f"{item['name']} x {item['qty']} @ Rs. {item['price']}", font_size=18))
        box.add_widget(Label(text=f"Total: Rs. {total}", font_size=24))
        confirm = Button(text="Confirm Order", font_size=20)
        back = Button(text="Back to Cart", font_size=20)

        popup = Popup(title="Confirm Order", content=box, size_hint=(0.9, 0.9))
        close_btn.bind(on_press=popup.dismiss)
        confirm.bind(on_press=lambda x: self.place_order_and_close(popup))
        back.bind(on_press=popup.dismiss)
        box.add_widget(confirm)
        box.add_widget(back)
        popup.open()

    def place_order_and_close(self, confirm_popup):
        order = place_order(self.username,
            [{"name": k, "qty": v, "price": self.get_price(k)} for k, v in self.cart.items()],
            self.selected_shop
        )
        order["payment"] = self.payment_method
        generate_pdf_bill(order)
        self.cart = {}
        confirm_popup.dismiss()
        if self.cart_popup:
            self.cart_popup.dismiss()
        self.show_bill_on_screen(order)

    def show_bill_on_screen(self, order):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        close_btn = Button(text="❌", size_hint_y=None, height=40, background_color=(1, 0, 0, 1), font_size=20)
        content.add_widget(Label(text="Super Grocery Mart", font_size=26))
        content.add_widget(Label(text=f"Customer: {order['user']}", font_size=20))
        content.add_widget(Label(text=f"Shop: {order['shop']}", font_size=20))
        content.add_widget(Label(text=f"Date: {date_str}  Time: {time_str}", font_size=18))
        content.add_widget(Label(text=f"Payment Mode: {order.get('payment', 'N/A')}", font_size=20))
        content.add_widget(Label(text="Items:", font_size=20))

        grand_total = 0
        for item in order["items"]:
            line = f"{item['name']} x {item['qty']} @ Rs. {item['price']} = Rs. {item['qty'] * item['price']}"
            grand_total += item["qty"] * item["price"]
            content.add_widget(Label(text=line, font_size=18))

        content.add_widget(Label(text=f"Total Amount: Rs. {grand_total}", font_size=24))
        content.add_widget(close_btn)

        popup = Popup(title="Order Receipt", content=content, size_hint=(0.9, 0.9))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

    def logout(self):
        self.manager.current = "login"

    def show_message(self, msg):
        content = BoxLayout(orientation="vertical", spacing=10)
        label = Label(text=msg, font_size=18)
        close_btn = Button(text="Close", size_hint_y=None, height=40, font_size=18)
        popup = Popup(title="Info", content=content, size_hint=(0.6, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(label)
        content.add_widget(close_btn)
        popup.open()
