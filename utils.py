import json
import os
import uuid
from datetime import datetime
import time
DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
ITEMS_FILE = os.path.join(DATA_DIR, "items.json")
ORDERS_FILE = os.path.join(DATA_DIR, "orders.json")
os.makedirs(os.path.dirname(ORDERS_FILE), exist_ok=True)
def _ensure_data_dir():
    os.makedirs(os.path.dirname(ORDERS_FILE), exist_ok=True)
    print(f"DEBUG: utils - Ensuring directory exists: {os.path.dirname(ORDERS_FILE)}")


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def load_items():
    if not os.path.exists(ITEMS_FILE):
        return []
    with open(ITEMS_FILE, "r") as f:
        return json.load(f)

def save_items(items):
    with open(ITEMS_FILE, "w") as f:
        json.dump(items, f, indent=2)

# def load_orders():
#     path = "data/orders.json"
#     if not os.path.exists(path):
#         return []
#     with open(path, "r") as f:
#         return json.load(f)

# def save_orders(orders):
#     with open("data/orders.json", "w") as f:
#         json.dump(orders, f, indent=2)

# def get_orders_for_shop(shop_name):
#     return [o for o in load_orders() if o["shop"] == shop_name]

# def update_order_status(order_id, new_status):
#     orders = load_orders()
#     for order in orders:
#         if order.get("id") == order_id:
#             order["status"] = new_status
#     save_orders(orders)
# def update_order_status(order_id, new_status, unavailable_items_list=None):
#     orders = load_orders()
#     updated_order = None
#     for order in orders:
#         if order.get("id") == order_id:
#             order["status"] = new_status
#
#             # --- Logic for handling unavailable items during status update ---
#             if unavailable_items_list:
#                 original_items = order["items"].copy() # Create a copy to iterate
#                 order["items"] = [] # Reset items for reconstruction
#                 total_price_adjustment = 0
#
#                 for item in original_items:
#                     if item["name"] in unavailable_items_list:
#                         # Item is marked unavailable, decide what to do:
#                         # Option 1: Completely remove the item (current implementation suggestion)
#                         total_price_adjustment -= (item["price"] * item["qty"]) # Subtract original item value
#                         # You could add a prompt here for partial availability if needed.
#                         # For now, it's just removed.
#                         print(f"Removed unavailable item: {item['name']} from order {order_id}")
#                     else:
#                         # Item is available, add it back to the list
#                         order["items"].append(item)
#
#                 # Re-calculate total price for the order if you have a total_price field
#                 # order["total_price"] = sum(i["price"] * i["qty"] for i in order["items"])
#
#             updated_order = order # Keep a reference to the updated order
#             break
#
#     if updated_order:
#         save_orders(orders)
#         return updated_order
#     return None # Return None if order not found

DATA_FILE = "data/orders.json"





# def save_orders(orders):
#     with open(DATA_FILE, "w") as f:
#         json.dump(orders, f, indent=4)


def place_order(username, items, shop):
    orders = load_orders()
    order_id = str(int(time.time() * 1000))  # unique timestamp-based ID

    total = sum(item["qty"] * item["price"] for item in items)
    order = {
        "id": order_id,
        "user": username,
        "shop": shop,
        "items": items,
        "total": total,
        "status": "Pending",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "shop_username": "shop1"
    }
    orders.append(order)
    save_orders(orders)
    return order


# def get_orders_for_shop(shop_name):
#     return [order for order in load_orders() if order["shop"] == shop_name and order["status"] != "Delivered"]


# def update_order_status(order_id, new_status, message=None):
#     orders = load_orders()
#     for order in orders:
#         if order.get("id") == order_id:
#             order["status"] = new_status
#             if message:
#                 order["message"] = message
#             break
#     save_orders(orders)



#
# def _ensure_data_dir():
#     os.makedirs(os.path.dirname(ORDERS_FILE), exist_ok=True)


# def load_orders():
#     _ensure_data_dir()
#     if not os.path.exists(ORDERS_FILE):
#         print(f"DEBUG: utils - Orders file not found: {ORDERS_FILE}")
#         return []
#     with open(ORDERS_FILE, "r") as f:
#         try:
#             orders = json.load(f)
#             print(f"DEBUG: utils - Loaded {len(orders)} orders from {ORDERS_FILE}")
#             # print(f"DEBUG: utils - Loaded orders content (first 500 chars): {str(orders)[:500]}") # Be careful with large data
#             return orders
#         except json.JSONDecodeError as e:
#             print(f"ERROR: utils - JSONDecodeError in {ORDERS_FILE}: {e}")
#             print(f"DEBUG: utils - Content of {ORDERS_FILE} (if readable): {f.read()}") # Attempt to read content if error
#             return []
#         except Exception as e:
#             print(f"ERROR: utils - Unexpected error loading orders: {e}")
#             return []


def load_orders():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"WARNING: '{ORDERS_FILE}' is empty or malformed JSON. Returning empty list.")
                return []
    return []


# def save_orders(orders):
#     _ensure_data_dir()
#     try:
#         with open(ORDERS_FILE, "w") as f:
#             json.dump(orders, f, indent=2)
#         print(f"DEBUG: utils - Saved {len(orders)} orders to {ORDERS_FILE}")
#     except Exception as e:
#         print(f"ERROR: utils - Failed to save orders: {e}")

def save_orders(orders):
    os.makedirs(os.path.dirname(ORDERS_FILE), exist_ok=True) # Ensure directory exists
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=2)

# def get_orders_for_shop(shop_username):
#     all_orders = load_orders()
#     print(f"DEBUG: utils - Filtering orders for shop: '{shop_username}'")
#     # This is the critical line. Double check the field name 'shop_username' in your actual data.
#     # If the shop sees ALL orders regardless of a 'shop_username' field, uncomment the next line:
#     # return all_orders
#     filtered = [o for o in all_orders if o.get("shop_username") == shop_username]
#     print(f"DEBUG: utils - Found {len(filtered)} orders for shop '{shop_username}' after filtering by 'shop_username' field.")
#     return filtered
def get_orders_for_shop(shop_username):
    all_orders = load_orders()
    print(f"DEBUG: utils - Filtering orders for shop: '{shop_username}'")
    # Uncomment the next line to make the shop see ALL orders
    return all_orders
    # filtered = [o for o in all_orders if o.get("shop_username") == shop_username]
    # print(f"DEBUG: utils - Found {len(filtered)} orders for shop '{shop_username}' after filtering by 'shop_username' field.")
   # return filtered

# def get_orders_for_shop(shop_username):
#     all_orders = load_orders()
#     return [order for order in all_orders if order.get("shop") == shop_username]

# MODIFIED: update_order_status now takes unavailable_items_list
# def update_order_status(order_id, new_status, unavailable_items_list=None):
#     orders = load_orders()
#     updated_order_data = None
#     for order in orders:
#         if order.get("id") == order_id:
#             order["status"] = new_status
#
#             # --- Handle unavailable items and price adjustment ---
#             if unavailable_items_list is not None and len(unavailable_items_list) > 0:
#                 print(f"Processing unavailable items for order {order_id}: {unavailable_items_list}")
#
#                 # Calculate new total price for the order after adjustments
#                 # (You might have a 'total_price' field in your order structure)
#                 # Let's assume original_total_price is calculated from current items
#
#                 new_items = []
#                 for item in order["items"]:
#                     if item["name"] in unavailable_items_list:
#                         # Item is marked unavailable.
#                         # Option 1: Completely remove the item.
#                         print(f"Item '{item['name']}' marked unavailable and removed from order {order_id}.")
#                         # If you need to log this removal somewhere else, do it here.
#                         # If you want partial availability, this is where you'd add a popup
#                         # or some logic to ask for the available quantity and adjust item details.
#                     else:
#                         new_items.append(item)
#                 order["items"] = new_items
#
#                 # Recalculate order total if you have a `total_price` field in your order dict
#                 # For example:
#                 # order["total_price"] = sum(item["price"] * item["qty"] for item in order["items"])
#
#             updated_order_data = order
#             break
#
#     if updated_order_data:
#         save_orders(orders)
#         return updated_order_data  # Return the updated order dictionary
#     return None  # Return None if order not found or not updated
def update_order_status(order_id, new_status, unavailable_items=None, updated_items=None):
    orders = load_orders()
    found_order = None
    for i, order in enumerate(orders):
        if order.get("id") == order_id:
            order["status"] = new_status
            if unavailable_items is not None:
                order["unavailable_items"] = unavailable_items
            if updated_items is not None:
                order["items"] = updated_items
                # Recalculate total_price if items were updated
                order["total_price"] = sum(item["price"] for item in order["items"])
            found_order = order
            break
    save_orders(orders)
    return found_order

# This function might not be strictly needed if update_order_status handles removals.
# If you decide to keep it for explicit item deletion:
def delete_order_item(order_id, item_name):
    orders = load_orders()
    item_removed = False
    for order in orders:
        if order.get("id") == order_id:
            original_items_count = len(order["items"])
            order["items"] = [item for item in order["items"] if item["name"] != item_name]
            if len(order["items"]) < original_items_count:
                item_removed = True
                # Recalculate order total here if you have a `total_price` field
                # order["total_price"] = sum(item["price"] * item["qty"] for item in order["items"])
            break
    if item_removed:
        save_orders(orders)
    return item_removed


def create_new_order(user, shop, items):
    """
    Example function to create a new order (assuming you have one like this).
    Ensure it adds order_time and unit_price for each item.
    """
    total_price = sum(item.get("price", item.get("qty", 0) * item.get("unit_price", 0)) for item in items)
    new_order = {
        "id": str(uuid.uuid4()),
        "user": user,
        "shop": shop,
        "items": items,
        "total_price": total_price,
        "status": "Order Received",
        "order_time": datetime.now().isoformat(),
        "unavailable_items": []
    }
    orders = load_orders()
    orders.append(new_order)
    save_orders(orders)
    return new_order