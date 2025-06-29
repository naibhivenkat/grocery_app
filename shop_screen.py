# import uuid
# import os
# import json
# from datetime import datetime, date
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.screenmanager import Screen
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.button import Button
# from kivy.uix.popup import Popup
# from kivy.uix.textinput import TextInput
# from kivy.uix.spinner import Spinner
# from kivy.properties import ObjectProperty
# from kivy.uix.image import Image
#
#
# # Assuming these are correctly implemented in utils.py
# from utils import get_orders_for_shop, update_order_status, save_orders, load_orders # delete_order_item is optional
#
# class ShopScreen(Screen):
#     customer_spinner_text = ObjectProperty("Select Customer")
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.shop_username = ""
#         self.selected_customer = None
#         self.all_orders_data = []
#
#     def set_user(self, username):
#         self.shop_username = username
#         self.selected_customer = None
#
#         self.customer_spinner_text = "Select Customer"
#         print(f"DEBUG: ShopScreen - Setting user: {username}")
#         self.all_orders_data = get_orders_for_shop(self.shop_username)
#         print(f"DEBUG: ShopScreen - Orders loaded for shop '{self.shop_username}': {len(self.all_orders_data)} orders.")
#         self.display_orders()
#
#     def display_orders(self):
#         self.clear_widgets()
#
#         main_layout = BoxLayout(orientation="vertical", spacing=15, padding=10) # Keep generous main spacing
#
#         # --- Top bar with customer filter ---
#         top_bar = BoxLayout(size_hint_y=None, height=70, spacing=15, padding=5) # Adjust height/spacing
#
#         unique_customers = list(
#             {o["user"] for o in self.all_orders_data if o["status"] != "Delivered" and not o["status"].startswith("Cancelled")}
#         )
#         unique_customers.sort()
#
#         print(f"DEBUG: ShopScreen - Unique active customers found: {unique_customers}")
#
#         spinner_values = ["Select Customer"] + unique_customers
#         cart_icon = Image(source="assets/dropdown.png", size_hint_x=0.3)
#         top_bar.add_widget(cart_icon)
#
#
#         customer_spinner = Spinner(
#             text=self.customer_spinner_text,
#             values=spinner_values,
#             size_hint_x=0.7,
#             font_size="22sp",
#         background_color = (0, 0, 1, 1)
#         )
#         customer_spinner.bind(text=self.on_customer_selected)
#         top_bar.add_widget(customer_spinner)
#
#         if self.selected_customer and self.selected_customer != "Select Customer":
#             back_to_all_btn = Button(
#                 text=" < Back to All",
#                 size_hint_x=0.3,
#                 font_size="18sp",
#                 on_press=self.reset_customer_filter,
#              background_color=(1, 0, 0, 1)
#             )
#             top_bar.add_widget(back_to_all_btn)
#         else:
#              top_bar.add_widget(BoxLayout(size_hint_x=0.3))
#
#         main_layout.add_widget(top_bar)
#
#         # --- Orders section (Scrollable) ---
#         # The main scroll view handles scrolling for the entire grid of order cards
#         scroll_view = ScrollView(do_scroll_x=False)
#
#         # GridLayout for arranging order cards.
#         # Now with cols=2 as you specified, and generous spacing.
#         order_container = GridLayout(cols=2, spacing=30, padding=10, size_hint_y=None)
#         order_container.bind(minimum_height=order_container.setter("height")) # Crucial for GridLayout within ScrollView
#
#         filtered_orders = []
#         if self.selected_customer and self.selected_customer != "Select Customer":
#             filtered_orders = [
#                 o for o in self.all_orders_data
#                 if o["user"] == self.selected_customer
#                    and not o.get("status", "").startswith("Cancelled")
#                    and o.get("status", "") != "Delivered"
#             ]
#
#         print(f"DEBUG: ShopScreen - Filtered orders for selected customer '{self.selected_customer}': {len(filtered_orders)} orders.")
#
#         if not filtered_orders:
#             # If no orders, display a single large label. It goes into order_container (which is cols=2, so it stretches)
#             order_container.add_widget(
#                 Label(text="Please select a customer to view orders,\n or no active orders found for this customer.",
#                       size_hint_y=None, height=150, font_size="18sp",
#                       valign="middle", halign="center", markup=True,
#                       size_hint_x=2) # Span across 2 columns if no orders
#             )
#         else:
#             status_options = ["Order Received", "Packing", "Delivered"]
#
#             for order in filtered_orders:
#                 order.setdefault("unavailable_items", [])
#
#                 # Define standard heights for fixed elements within an order box
#                 HEADER_HEIGHT = 50 # Height for Customer/Order ID
#                 ITEM_LABEL_HEIGHT = 40 # Height for "Items:" label
#                 ITEM_ROW_HEIGHT = 50 # Height for each item line (label + button)
#                 STATUS_SPINNER_HEIGHT = 60 # Height for status dropdown
#                 CANCEL_BUTTON_HEIGHT = 60 # Height for cancel button
#                 BOX_VERTICAL_PADDING = 50 # Sum of top/bottom padding for the box (25 top + 25 bottom)
#                 BOX_VERTICAL_SPACING = 50 # Sum of spacing between major elements in box (e.g., 4*15=60 or similar)
#
#                 # Max height for the items scroll view within the box
#                 # Let's limit it to display about 3-4 items before it scrolls
#                 MAX_ITEMS_SCROLL_HEIGHT = 4 * ITEM_ROW_HEIGHT + 10 # 4 items + some padding/spacing
#
#                 # Calculate the height for the inner item_scroll_view
#                 # It will be either its full content height or the MAX_ITEMS_SCROLL_HEIGHT
#                 calculated_items_scroll_height = min(len(order["items"]) * ITEM_ROW_HEIGHT, MAX_ITEMS_SCROLL_HEIGHT)
#                 if len(order["items"]) * ITEM_ROW_HEIGHT == 0: # Handle no items in order
#                      calculated_items_scroll_height = ITEM_ROW_HEIGHT # Give it a min height for visibility if empty
#
#
#                 # Calculate total height for the outer box
#                 # Sum of all fixed height elements plus the calculated item list height
#                 estimated_box_height = (
#                     HEADER_HEIGHT +
#                     ITEM_LABEL_HEIGHT +
#                     calculated_items_scroll_height + # This is the key
#                     STATUS_SPINNER_HEIGHT +
#                     CANCEL_BUTTON_HEIGHT +
#                     BOX_VERTICAL_PADDING +
#                     BOX_VERTICAL_SPACING # Adjust this based on overall spacing within the box
#                 )
#
#                 # Ensure a reasonable minimum height for the entire order box
#                 if estimated_box_height < 450: # Adjust this minimum as needed
#                     estimated_box_height = 450
#
#
#                 box = BoxLayout(orientation="vertical", size_hint_y=None, height=estimated_box_height,
#                                 padding=25, spacing=15) # Adjusted padding and spacing for the box
#
#                 # Customer and Order ID Header
#                 box.add_widget(Label(
#                     text=f"[b]Customer:[/b] {order['user']}\n[b]Order ID:[/b] {order.get('id', 'N/A')}",
#                     markup=True, size_hint_y=None, height=HEADER_HEIGHT, font_size="18sp",
#                     halign="left", valign="top"
#                 ))
#
#                 # Label for Items section
#                 box.add_widget(Label(text="[b]Items:[/b]", markup=True, size_hint_y=None, height=ITEM_LABEL_HEIGHT, font_size="20sp", halign="left"))
#
#                 # Container for the actual items, now using the calculated height
#                 items_scroll_view = ScrollView(size_hint_y=None, height=calculated_items_scroll_height)
#                 items_grid = GridLayout(cols=1, size_hint_y=None, spacing=5) # Smaller spacing for items
#                 items_grid.bind(minimum_height=items_grid.setter("height")) # Ensure items_grid expands inside its scrollview
#
#
#                 for item in order["items"]:
#                     item_line = f"- {item['name']} x {item['qty']} = ₹{item['price'] * item['qty']}"
#                     item_layout = BoxLayout(size_hint_y=None, height=ITEM_ROW_HEIGHT, padding=(20,0,0,0)) # Padding to indent
#                     item_label = Label(text=item_line, halign="left", valign="middle", size_hint_x=0.7, font_size="18sp")
#
#                     unavailable_btn = Button(
#                         text="Unavailable" if item["name"] in order["unavailable_items"] else "Mark Unavailable",
#                         size_hint_x=None,
#                         width=180,
#                         font_size="18sp",
#                         background_color=(1, 0.5, 0.5, 1) if item["name"] in order["unavailable_items"] else (0.2, 0.7, 0.9, 1)
#                     )
#                     unavailable_btn.bind(on_press=lambda btn, item_n=item["name"], ord=order, b_inst=unavailable_btn: self.toggle_unavailable_item(b_inst, item_n, ord))
#
#                     item_layout.add_widget(item_label)
#                     item_layout.add_widget(unavailable_btn)
#                     items_grid.add_widget(item_layout)
#
#                 items_scroll_view.add_widget(items_grid)
#                 box.add_widget(items_scroll_view)
#
#                 # Order Status Dropdown (Spinner)
#                 status_spinner = Spinner(
#                     text=order["status"],
#                     values=status_options,
#                     size_hint_y=None,
#                     height=STATUS_SPINNER_HEIGHT,
#                     font_size="20sp"
#                 )
#                 status_spinner.bind(text=lambda spinner, new_status, o=order: self.update_order_status_from_spinner(o, new_status))
#                 box.add_widget(status_spinner)
#
#                 # Cancel Order button
#                 cancel_btn = Button(text="Cancel Order", background_color=(1, 0, 0, 1), size_hint_y=None, height=CANCEL_BUTTON_HEIGHT, font_size="20sp")
#                 cancel_btn.bind(on_press=lambda inst, o=order: self.show_cancel_popup(o))
#                 box.add_widget(cancel_btn)
#
#                 order_container.add_widget(box)
#
#         scroll_view.add_widget(order_container)
#         main_layout.add_widget(scroll_view)
#
#         # --- Bottom bar: Logout button ---
#         bottom_bar = BoxLayout(size_hint_y=None, height=70, padding=10, spacing=20)
#         logout_btn = Button(text="Logout", size_hint_x=1, font_size="22sp")
#         logout_btn.bind(on_press=self.logout)
#         bottom_bar.add_widget(logout_btn)
#         main_layout.add_widget(bottom_bar)
#
#         self.add_widget(main_layout)
#
#     def on_customer_selected(self, spinner, text):
#         if text == "Select Customer":
#             self.selected_customer = None
#             self.customer_spinner_text = "Select Customer"
#         else:
#             self.selected_customer = text
#             self.customer_spinner_text = text
#         self.display_orders()
#
#     def reset_customer_filter(self, *args):
#         self.selected_customer = None
#         self.customer_spinner_text = "Select Customer"
#         self.display_orders()
#
#     def update_order_status_from_spinner(self, order, new_status):
#         self.update_order(order, new_status)
#
#     def toggle_unavailable_item(self, btn_instance, item_name, current_order):
#         if item_name in current_order["unavailable_items"]:
#             current_order["unavailable_items"].remove(item_name)
#             btn_instance.text = "Mark Unavailable"
#             btn_instance.background_color = (0.2, 0.7, 0.9, 1)
#         else:
#             current_order["unavailable_items"].append(item_name)
#             btn_instance.text = "Unavailable"
#             btn_instance.background_color = (1, 0.5, 0.5, 1)
#
#         for i, ord in enumerate(self.all_orders_data):
#             if ord.get("id") == current_order.get("id"):
#                 self.all_orders_data[i] = current_order
#                 break
#         save_orders(self.all_orders_data)
#
#     def update_order(self, order, new_status):
#         order_id = order.get("id")
#         if not order_id:
#             order_id = str(uuid.uuid4())
#             order["id"] = order_id
#             for o in self.all_orders_data:
#                 if o is order:
#                     o["id"] = order_id
#                     break
#
#         updated_order = update_order_status(order["id"], new_status, order.get("unavailable_items", []))
#
#         if updated_order:
#             for i, ord in enumerate(self.all_orders_data):
#                 if ord.get("id") == updated_order.get("id"):
#                     self.all_orders_data[i] = updated_order
#                     break
#
#         self.display_orders()
#
#     def show_cancel_popup(self, order):
#         content = BoxLayout(orientation="vertical", spacing=15, padding=15)
#         msg_input = TextInput(hint_text="Enter reason for cancellation", multiline=True, size_hint_y=0.7, font_size="18sp")
#         content.add_widget(msg_input)
#
#         btns = BoxLayout(size_hint_y=None, height=60, spacing=15)
#         confirm = Button(text="Confirm", font_size="20sp")
#         cancel = Button(text="Dismiss", font_size="20sp")
#
#         btns.add_widget(confirm)
#         btns.add_widget(cancel)
#         content.add_widget(btns)
#
#         popup = Popup(title="Cancel Order", content=content, size_hint=(0.9, 0.65))
#         confirm.bind(on_press=lambda x: self.confirm_cancel(order, msg_input.text, popup))
#         cancel.bind(on_press=popup.dismiss)
#         popup.open()
#
#     def confirm_cancel(self, order, msg, popup):
#         self.log_cancelled_order(order, msg)
#         updated_order = update_order_status(order["id"], f"Cancelled: {msg}")
#
#         self.all_orders_data = [o for o in self.all_orders_data if o.get("id") != order["id"]]
#         save_orders(self.all_orders_data)
#
#         popup.dismiss()
#         self.display_orders()
#
#     def log_cancelled_order(self, order, message):
#         cancelled_path = "data/cancelled_orders.json"
#         os.makedirs(os.path.dirname(cancelled_path), exist_ok=True)
#
#         cancelled = []
#         if os.path.exists(cancelled_path):
#             with open(cancelled_path, "r") as f:
#                 try:
#                     cancelled = json.load(f)
#                 except json.JSONDecodeError:
#                     print(f"WARNING: '{cancelled_path}' is empty or malformed. Initializing as empty list.")
#                     cancelled = []
#
#         cancelled_order_copy = order.copy()
#         cancelled_order_copy["cancel_message"] = message
#         cancelled_order_copy["cancel_time"] = datetime.now().isoformat()
#         cancelled.append(cancelled_order_copy)
#
#         with open(cancelled_path, "w") as f:
#             json.dump(cancelled, f, indent=2)
#
#     def logout(self, *args):
#         self.manager.current = "login"
#
#     def consolidate_daily_orders(self, orders_list):
#         consolidated = {}
#         for order in orders_list:
#             order_date_str = datetime.fromisoformat(order["order_time"]).date().isoformat()
#             customer_id = order["user"]
#             key = (order_date_str, customer_id)
#
#             if key not in consolidated:
#                 consolidated[key] = {
#                     "id": str(uuid.uuid4()),
#                     "user": customer_id,
#                     "shop": order["shop"],
#                     "status": "Order received",
#                     "order_time": order["order_time"],
#                     "items": [],
#                     "unavailable_items": [],
#                     "original_order_ids": [order.get("id")]
#                 }
#             else:
#                 consolidated[key]["original_order_ids"].append(order.get("id"))
#
#             for item in order["items"]:
#                 found_item = False
#                 for existing_item in consolidated[key]["items"]:
#                     if existing_item["name"] == item["name"]:
#                         existing_item["qty"] += item["qty"]
#                         found_item = True
#                         break
#                 if not found_item:
#                     consolidated[key]["items"].append(item.copy())
#
#         return list(consolidated.values())

import uuid
import os
import json
from datetime import datetime, date
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.metrics import dp


# Assuming these are correctly implemented in utils.py
from utils import get_orders_for_shop, update_order_status, save_orders, load_orders # delete_order_item is optional

class ShopScreen(Screen):
    customer_spinner_text = ObjectProperty("Select Customer")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shop_username = ""
        self.selected_customer = None
        self.all_orders_data = []

    def set_user(self, username):
        self.shop_username = username
        self.selected_customer = None

        self.customer_spinner_text = "Select Customer"
        print(f"DEBUG: ShopScreen - Setting user: {username}")
        self.all_orders_data = get_orders_for_shop(self.shop_username)
        print(f"DEBUG: ShopScreen - Orders loaded for shop '{self.shop_username}': {len(self.all_orders_data)} orders.")
        self.display_orders()

    def display_orders(self):
        self.clear_widgets()

        main_layout = BoxLayout(orientation="vertical", spacing=dp(15), padding=dp(10))

        # --- Top bar with customer filter ---
        top_bar = BoxLayout(size_hint_y=None, height=dp(70), spacing=dp(15), padding=dp(5))

        unique_customers = list(
            {o["user"] for o in self.all_orders_data if o["status"] != "Delivered" and not o["status"].startswith("Cancelled")}
        )
        unique_customers.sort()

        print(f"DEBUG: ShopScreen - Unique active customers found: {unique_customers}")

        spinner_values = ["Select Customer"] + unique_customers
        cart_icon = Image(source="assets/dropdown.png", size_hint_x=0.3)
        top_bar.add_widget(cart_icon)


        customer_spinner = Spinner(
            text=self.customer_spinner_text,
            values=spinner_values,
            size_hint_x=0.7,
            font_size="22sp",
            background_color = (0, 0, 1, 1)
        )
        customer_spinner.bind(text=self.on_customer_selected)
        top_bar.add_widget(customer_spinner)

        if self.selected_customer and self.selected_customer != "Select Customer":
            back_to_all_btn = Button(
                text=" < Back to All",
                size_hint_x=0.3,
                font_size="18sp",
                on_press=self.reset_customer_filter,
                background_color=(1, 0, 0, 1)
            )
            top_bar.add_widget(back_to_all_btn)
        else:
             top_bar.add_widget(BoxLayout(size_hint_x=0.3))

        main_layout.add_widget(top_bar)

        # --- Orders section (Scrollable) ---
        scroll_view = ScrollView(do_scroll_x=False)

        order_container = GridLayout(cols=2, spacing=dp(30), padding=dp(10), size_hint_y=None)
        order_container.bind(minimum_height=order_container.setter("height"))

        filtered_orders = []
        if self.selected_customer and self.selected_customer != "Select Customer":
            filtered_orders = [
                o for o in self.all_orders_data
                if o["user"] == self.selected_customer
                   and not o.get("status", "").startswith("Cancelled")
                   and o.get("status", "") != "Delivered"
            ]

        print(f"DEBUG: ShopScreen - Filtered orders for selected customer '{self.selected_customer}': {len(filtered_orders)} orders.")

        if not filtered_orders:
            order_container.add_widget(
                Label(text="Please select a customer to view orders,\n or no active orders found for this customer.",
                      size_hint_y=None, height=dp(150), font_size="18sp",
                      valign="middle", halign="center", markup=True,
                      size_hint_x=2)
            )
        else:
            status_options = ["Order Received", "Packing", "Delivered"]

            for order in filtered_orders:
                order.setdefault("unavailable_items", []) # Ensure this key exists

                # Define standard heights for fixed elements within an order box
                HEADER_HEIGHT = dp(50) # Height for Customer/Order ID
                DATE_TIME_HEIGHT = dp(40) # Height for Date and Time
                ITEM_LABEL_HEIGHT = dp(40) # Height for "Items:" label
                ITEM_ROW_HEIGHT = dp(50) # Height for each item line (label + button)
                STATUS_SPINNER_HEIGHT = dp(60) # Height for status dropdown
                CANCEL_BUTTON_HEIGHT = dp(60) # Height for cancel button
                BOX_VERTICAL_PADDING = dp(50) # Sum of top/bottom padding for the box (25 top + 25 bottom)
                BOX_VERTICAL_SPACING = dp(50) # Sum of spacing between major elements in box (e.g., 4*15=60 or similar)

                # Max height for the items scroll view within the box
                MAX_ITEMS_SCROLL_HEIGHT = 4 * ITEM_ROW_HEIGHT + dp(10) # 4 items + some padding/spacing

                # Calculate the height for the inner item_scroll_view
                calculated_items_scroll_height = min(len(order["items"]) * ITEM_ROW_HEIGHT, MAX_ITEMS_SCROLL_HEIGHT)
                if len(order["items"]) * ITEM_ROW_HEIGHT == 0: # Handle no items in order
                     calculated_items_scroll_height = ITEM_ROW_HEIGHT # Give it a min height for visibility if empty


                # Calculate total height for the outer box
                estimated_box_height = (
                    HEADER_HEIGHT +
                    DATE_TIME_HEIGHT + # Added height for date/time
                    ITEM_LABEL_HEIGHT +
                    calculated_items_scroll_height +
                    STATUS_SPINNER_HEIGHT +
                    CANCEL_BUTTON_HEIGHT +
                    BOX_VERTICAL_PADDING +
                    BOX_VERTICAL_SPACING
                )

                if estimated_box_height < dp(450):
                    estimated_box_height = dp(450)


                box = BoxLayout(orientation="vertical", size_hint_y=None, height=estimated_box_height,
                                padding=dp(25), spacing=dp(15))

                # Customer and Order ID Header - Centered
                box.add_widget(Label(
                    text=f"[b]Customer:[/b] {order['user']}\n[b]Order ID:[/b] {order.get('id', 'N/A')}",
                    markup=True, size_hint_y=None, height=HEADER_HEIGHT, font_size="18sp",
                    halign="center", valign="middle" # Centered
                ))

                # Order Date and Time - Make robust to missing order_time
                order_time_str = order.get("order_time", None)
                if order_time_str:
                    try:
                        order_dt = datetime.fromisoformat(order_time_str)
                        date_time_text = f"[b]Date:[/b] {order_dt.strftime('%d-%m-%Y')}\n[b]Time:[/b] {order_dt.strftime('%I:%M %p')}"
                    except ValueError:
                        date_time_text = "[b]Date/Time:[/b] Invalid Format"
                else:
                    date_time_text = "[b]Date/Time:[/b] Not Available"

                box.add_widget(Label(
                    text=date_time_text,
                    markup=True, size_hint_y=None, height=DATE_TIME_HEIGHT, font_size="16sp",
                    halign="center", valign="middle"
                ))

                # Label for Items section
                box.add_widget(Label(text="[b]Items:[/b]", markup=True, size_hint_y=None, height=ITEM_LABEL_HEIGHT, font_size="20sp", halign="left"))

                items_scroll_view = ScrollView(size_hint_y=None, height=calculated_items_scroll_height)
                items_grid = GridLayout(cols=1, size_hint_y=None, spacing=dp(5))
                items_grid.bind(minimum_height=items_grid.setter("height"))


                # Item numbering
                for idx, item in enumerate(order["items"]):
                    item_line = f"{idx + 1}. {item['name']} x {item['qty']} = ₹{item['price']:.2f}"
                    item_layout = BoxLayout(size_hint_y=None, height=ITEM_ROW_HEIGHT, padding=(dp(20),0,0,0))
                    item_label = Label(text=item_line, halign="left", valign="middle", size_hint_x=0.7, font_size="18sp")

                    unavailable_btn = Button(
                        text="Unavailable" if item["name"] in order["unavailable_items"] else "Mark Unavailable",
                        size_hint_x=None,
                        width=dp(180),
                        font_size="18sp",
                        background_color=(1, 0.5, 0.5, 1) if item["name"] in order["unavailable_items"] else (0.2, 0.7, 0.9, 1)
                    )
                    unavailable_btn.bind(on_press=lambda btn, item_n=item["name"], ord=order: self.toggle_unavailable_item(btn, item_n, ord))

                    item_layout.add_widget(item_label)
                    item_layout.add_widget(unavailable_btn)
                    items_grid.add_widget(item_layout)

                items_scroll_view.add_widget(items_grid)
                box.add_widget(items_scroll_view)

                # Order Status Dropdown (Spinner) - Aligned Left
                status_spinner = Spinner(
                    text=order["status"],
                    values=status_options,
                    size_hint_y=None,
                    height=STATUS_SPINNER_HEIGHT,
                    font_size="20sp",
                    halign="left", # Left aligned
                    text_size=(box.width - dp(50), STATUS_SPINNER_HEIGHT) # Adjust text_size to make halign work
                )
                status_spinner.bind(text=lambda spinner, new_status, o=order: self.update_order_status_from_spinner(o, new_status))
                box.add_widget(status_spinner)

                # Cancel Order button
                cancel_btn = Button(text="Cancel Order", background_color=(1, 0, 0, 1), size_hint_y=None, height=CANCEL_BUTTON_HEIGHT, font_size="20sp")
                cancel_btn.bind(on_press=lambda inst, o=order: self.show_cancel_popup(o))
                box.add_widget(cancel_btn)

                order_container.add_widget(box)

        scroll_view.add_widget(order_container)
        main_layout.add_widget(scroll_view)

        # --- Bottom bar: Logout button ---
        bottom_bar = BoxLayout(size_hint_y=None, height=dp(70), padding=dp(10), spacing=dp(20))
        logout_btn = Button(text="Logout", size_hint_x=1, font_size="22sp")
        logout_btn.bind(on_press=self.logout)
        bottom_bar.add_widget(logout_btn)
        main_layout.add_widget(bottom_bar)

        self.add_widget(main_layout)

    def on_customer_selected(self, spinner, text):
        if text == "Select Customer":
            self.selected_customer = None
            self.customer_spinner_text = "Select Customer"
        else:
            self.selected_customer = text
            self.customer_spinner_text = text
        self.display_orders()

    def reset_customer_filter(self, *args):
        self.selected_customer = None
        self.customer_spinner_text = "Select Customer"
        self.display_orders()

    def update_order_status_from_spinner(self, order, new_status):
        self.update_order(order, new_status)

    def toggle_unavailable_item(self, btn_instance, item_name, current_order):
        # Find the specific item in the current_order's items list
        item_to_toggle = None
        for item in current_order["items"]:
            if item["name"] == item_name:
                item_to_toggle = item
                break

        if not item_to_toggle:
            print(f"Error: Item '{item_name}' not found in order {current_order.get('id')}")
            return

        if item_name in current_order["unavailable_items"]:
            # If already marked unavailable, revert it
            current_order["unavailable_items"].remove(item_name)
            # Restore the original quantity and price of the item if it was adjusted
            # This requires knowing the *original* state of the item.
            # For simplicity now, we'll re-add it fully if it was previously removed
            # or simply mark it as available again if quantity was reduced.
            # A more robust solution might involve storing the original quantity/price
            # within the 'unavailable_items' list or a separate structure.
            # For now, we'll assume making it 'available' means restoring its state
            # from the most recent full order, which implies it will reappear in display_orders.
            self.display_orders() # Refresh display to show it as available again
        else:
            # If not unavailable, show popup to adjust quantity
            self.show_item_quantity_popup(btn_instance, item_name, current_order)


    def show_item_quantity_popup(self, btn_instance, item_name, current_order):
        original_item_qty = 0
        current_item_price = 0.0 # To get the current total price of the item in the order
        for item in current_order["items"]:
            if item["name"] == item_name:
                original_item_qty = item["qty"]
                current_item_price = item["price"]
                break

        content = BoxLayout(orientation="vertical", spacing=dp(15), padding=dp(15))
        content.add_widget(Label(text=f"Adjust quantity for '{item_name}':\n (Current: {original_item_qty})",
                                 size_hint_y=None, height=dp(60), font_size="18sp", halign="center"))
        qty_input = TextInput(hint_text="Enter available quantity (0 to remove)",
                              multiline=False, input_type="number", size_hint_y=None, height=dp(50), font_size="18sp")
        qty_input.text = str(original_item_qty) # Pre-fill with current quantity
        content.add_widget(qty_input)

        btns = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(15))
        confirm = Button(text="Confirm", font_size="20sp")
        cancel = Button(text="Dismiss", font_size="20sp")

        btns.add_widget(confirm)
        btns.add_widget(cancel)
        content.add_widget(btns)

        popup = Popup(title="Adjust Item Quantity", content=content, size_hint=(0.9, 0.65))
        confirm.bind(on_press=lambda x: self.confirm_quantity_update(popup, qty_input.text, item_name, current_order))
        cancel.bind(on_press=popup.dismiss)
        popup.open()


    def confirm_quantity_update(self, popup, new_qty_str, item_name, current_order):
        try:
            new_qty = int(new_qty_str)
        except ValueError:
            new_qty = -1 # Indicate invalid input

        if new_qty < 0:
            # Show an error message if the input is invalid
            error_popup = Popup(title="Invalid Quantity",
                                content=Label(text="Please enter a valid non-negative number for quantity."),
                                size_hint=(0.7, 0.3))
            error_popup.open()
            return

        original_order_items = current_order["items"][:] # Create a copy to iterate
        updated_items = []
        item_unit_price = 0.0 # To store the unit price of the item being adjusted

        for item in original_order_items:
            if item["name"] == item_name:
                # Determine unit_price: prefer 'unit_price' if it exists, otherwise calculate from 'price' and 'qty'
                if "unit_price" in item and item["unit_price"] is not None:
                    item_unit_price = item["unit_price"]
                elif item["qty"] > 0: # Avoid division by zero
                    item_unit_price = item["price"] / item["qty"]
                else:
                    item_unit_price = 0.0 # Default if quantity is zero and no unit_price

                if new_qty == 0:
                    # Item is fully unavailable, remove from items list and add to unavailable_items
                    if item_name not in current_order["unavailable_items"]:
                        current_order["unavailable_items"].append(item_name)
                    print(f"DEBUG: Removed '{item_name}' from order {current_order.get('id')}")
                else:
                    # Update quantity and recalculate price for this item
                    item_copy = item.copy()
                    item_copy["qty"] = new_qty
                    item_copy["price"] = item_unit_price * new_qty # Use calculated/retrieved unit_price
                    item_copy["unit_price"] = item_unit_price # Ensure unit_price is stored for future edits
                    updated_items.append(item_copy)
                    # Remove from unavailable_items if it was there (since it's now partially available)
                    if item_name in current_order["unavailable_items"]:
                        current_order["unavailable_items"].remove(item_name)
                    print(f"DEBUG: Updated '{item_name}' in order {current_order.get('id')} to quantity {new_qty}")
            else:
                updated_items.append(item.copy())

        current_order["items"] = updated_items

        # Recalculate the overall total price for the order based on updated_items
        new_total_price = sum(item["price"] for item in updated_items)
        current_order["total_price"] = new_total_price

        # Update the order in the main data structure and save
        for i, ord in enumerate(self.all_orders_data):
            if ord.get("id") == current_order.get("id"):
                self.all_orders_data[i] = current_order
                break
        save_orders(self.all_orders_data)
        popup.dismiss()
        self.display_orders() # Refresh the display

    def update_order(self, order, new_status):
        order_id = order.get("id")
        if not order_id:
            order_id = str(uuid.uuid4())
            order["id"] = order_id
            for o in self.all_orders_data:
                if o is order:
                    o["id"] = order_id
                    break

        # When updating order status, we also pass the potentially modified items list
        # and unavailable_items list to the utility function.
        # It's crucial that your `update_order_status` in `utils.py` handles these arguments
        # and correctly updates the order in your storage (JSON file).
        updated_order = update_order_status(
            order["id"],
            new_status,
            order.get("unavailable_items", []),
            order["items"] # Pass the current items list as well
        )

        if updated_order:
            for i, ord in enumerate(self.all_orders_data):
                if ord.get("id") == updated_order.get("id"):
                    self.all_orders_data[i] = updated_order
                    break
        save_orders(self.all_orders_data) # Save changes after update_order_status might modify the order
        self.display_orders()

    def show_cancel_popup(self, order):
        content = BoxLayout(orientation="vertical", spacing=dp(15), padding=dp(15))
        msg_input = TextInput(hint_text="Enter reason for cancellation", multiline=True, size_hint_y=0.7, font_size="18sp")
        content.add_widget(msg_input)

        btns = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(15))
        confirm = Button(text="Confirm", font_size="20sp")
        cancel = Button(text="Dismiss", font_size="20sp")

        btns.add_widget(confirm)
        btns.add_widget(cancel)
        content.add_widget(btns)

        popup = Popup(title="Cancel Order", content=content, size_hint=(0.9, 0.65))
        confirm.bind(on_press=lambda x: self.confirm_cancel(order, msg_input.text, popup))
        cancel.bind(on_press=popup.dismiss)
        popup.open()

    def confirm_cancel(self, order, msg, popup):
        self.log_cancelled_order(order, msg)
        # Pass the original items and unavailable items when cancelling for logging purposes
        updated_order = update_order_status(
            order["id"],
            f"Cancelled: {msg}",
            order.get("unavailable_items", []),
            order["items"] # Pass the current items list for logging
        )

        # Remove the cancelled order from the list of active orders
        self.all_orders_data = [o for o in self.all_orders_data if o.get("id") != order["id"]]
        save_orders(self.all_orders_data) # Save the modified list

        popup.dismiss()
        self.display_orders()

    def log_cancelled_order(self, order, message):
        cancelled_path = "data/cancelled_orders.json"
        os.makedirs(os.path.dirname(cancelled_path), exist_ok=True)

        cancelled = []
        if os.path.exists(cancelled_path):
            with open(cancelled_path, "r") as f:
                try:
                    cancelled = json.load(f)
                except json.JSONDecodeError:
                    print(f"WARNING: '{cancelled_path}' is empty or malformed. Initializing as empty list.")
                    cancelled = []

        cancelled_order_copy = order.copy()
        cancelled_order_copy["cancel_message"] = message
        cancelled_order_copy["cancel_time"] = datetime.now().isoformat()
        cancelled.append(cancelled_order_copy)

        with open(cancelled_path, "w") as f:
            json.dump(cancelled, f, indent=2)

    def logout(self, *args):
        self.manager.current = "login"

    def consolidate_daily_orders(self, orders_list):
        consolidated = {}
        for order in orders_list:
            # Safely get order_time, default to current time if missing for consolidation
            order_time_str = order.get("order_time", datetime.now().isoformat())
            try:
                order_date_str = datetime.fromisoformat(order_time_str).date().isoformat()
            except ValueError:
                # Fallback if isoformat is invalid for existing data
                print(f"WARNING: Invalid order_time format '{order_time_str}' for order {order.get('id')}. Using current date for consolidation.")
                order_date_str = datetime.now().date().isoformat()

            customer_id = order["user"]
            key = (order_date_str, customer_id)

            if key not in consolidated:
                consolidated[key] = {
                    "id": str(uuid.uuid4()),
                    "user": customer_id,
                    "shop": order["shop"],
                    "status": "Order received",
                    "order_time": order_time_str, # Use the original or default time
                    "items": [],
                    "unavailable_items": [],
                    "original_order_ids": [order.get("id")]
                }
            else:
                consolidated[key]["original_order_ids"].append(order.get("id"))

            for item in order["items"]:
                found_item = False
                for existing_item in consolidated[key]["items"]:
                    if existing_item["name"] == item["name"]:
                        existing_item["qty"] += item["qty"]
                        existing_item["price"] += item["price"]
                        # If unit_price exists, ensure it's handled during consolidation
                        # For simplicity, if unit_price is missing in existing, calculate it from new item.
                        # For complex scenarios, might need average or prioritizing newer data.
                        if "unit_price" in item and ("unit_price" not in existing_item or existing_item["unit_price"] is None):
                            existing_item["unit_price"] = item["unit_price"]
                        elif "unit_price" not in existing_item and existing_item["qty"] > 0:
                            existing_item["unit_price"] = existing_item["price"] / existing_item["qty"]
                        found_item = True
                        break
                if not found_item:
                    item_copy = item.copy()
                    # Ensure unit_price is copied if it exists in the original item
                    if "unit_price" not in item_copy and item_copy.get("qty", 0) > 0:
                        item_copy["unit_price"] = item_copy["price"] / item_copy["qty"]
                    consolidated[key]["items"].append(item_copy)

        return list(consolidated.values())