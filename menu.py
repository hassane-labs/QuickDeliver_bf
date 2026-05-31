# =============================================================================
# QuickDeliver_BF — DELIVERY MANAGEMENT SYSTEM
# menu.py — User interaction functions (input handling and display)
# Members : Cheick, Ezekiel, Hassane, Nina, Nimatou
# Burkina Institute of Technology
# =============================================================================

from models import Client, Courier, Parcel, Delivery, VALID_STATUSES
from file_handler import save_delivery, save_report
from utils import (validate_phone, validate_email, validate_weight,
                   display_separator, display_title,
                   find_available_courier, find_delivery_by_id)


# =============================================================================
#                           MAIN MENU — by Hassane
# =============================================================================

def display_main_menu():
    """Displays the QuickDeliver_BF main menu with all available options."""
    print("\n" + "=" * 60)
    print("QuickDeliver_BF — MAIN MENU")
    print("=" * 60)
    print("  1. Add a new client")
    print("  2. Add a new courier")
    print("  3. Create a new delivery")
    print("  4. Track a delivery")
    print("  5. Update delivery status")
    print("  6. View all clients")
    print("  7. View all couriers")
    print("  8. View all deliveries")
    print("  9. Generate report")
    print("  0. Quit")
    print("-" * 60)


# =============================================================================
# CLIENT FUNCTIONS — by Cheick
# =============================================================================

def input_client(clients: list) -> Client:
    """
    Prompts the user to enter information for a new client
    and returns the created Client object.

    Args:
        clients (list): The existing list of clients.

    Returns:
        Client: The newly created Client object.
    """
    display_title("Add a New Client")

    last_name: str = input("  Last name    : ").strip()
    while not last_name:
        print("  Last name cannot be empty.")
        last_name = input("  Last name    : ").strip()

    first_name: str = input("  First name   : ").strip()
    while not first_name:
        print("  First name cannot be empty.")
        first_name = input("  First name   : ").strip()

    phone: str = input("  Phone (8 digits) : ").strip()
    while not validate_phone(phone):
        print("  Phone number must contain exactly 8 digits.")
        phone = input("  Phone (8 digits) : ").strip()

    email: str = input("  Email        : ").strip()
    while not validate_email(email):
        print("  Invalid email — must contain '@' and '.'.")
        email = input("  Email        : ").strip()

    address: str = input("  Address      : ").strip()
    while not address:
        print("  Address cannot be empty.")
        address = input("  Address      : ").strip()

    new_client = Client(last_name, first_name, phone, email, address)
    print(f"\n  Client {first_name} {last_name} added successfully! (ID: {new_client.get_client_id()})")
    return new_client


def display_all_clients(clients: list):
    """
    Displays the full list of all registered clients.
    Shows a message if no clients are registered yet.

    Args:
        clients (list): The list of all Client objects.
    """
    display_title("All Registered Clients")

    if not clients:
        print("  No clients registered yet.")
        return

    for index, client in enumerate(clients, start=1):
        print(f"\n  --- Client #{index} ---")
        client.display_info()
        display_separator()





# COURIER FUNCTIONS — by Ezekiel


def input_courier(couriers: list) -> Courier:
    """
    Prompts the user to enter information for a new courier
    and returns the created Courier object.

    Args:
        couriers (list): The existing list of couriers.

    Returns:
        Courier: The newly created Courier object.
    """
    display_title("Add a New Courier")

    last_name: str = input("  Last name    : ").strip()
    while not last_name:
        print("  Last name cannot be empty.")
        last_name = input("  Last name    : ").strip()

    first_name: str = input("  First name   : ").strip()
    while not first_name:
        print("  First name cannot be empty.")
        first_name = input("  First name   : ").strip()

    phone: str = input("  Phone (8 digits) : ").strip()
    while not validate_phone(phone):
        print("  Phone number must contain exactly 8 digits.")
        phone = input("  Phone (8 digits) : ").strip()

    email: str = input("  Email        : ").strip()
    while not validate_email(email):
        print("  Invalid email — must contain '@' and '.'.")
        email = input("  Email        : ").strip()

    vehicle: str = input("  Vehicle type (motorbike / car / bicycle) : ").strip()
    while not vehicle:
        print("  Vehicle type cannot be empty.")
        vehicle = input("  Vehicle type : ").strip()

    zone: str = input("  Delivery zone : ").strip()
    while not zone:
        print("  Delivery zone cannot be empty.")
        zone = input("  Delivery zone : ").strip()

    new_courier = Courier(last_name, first_name, phone, email, vehicle, zone)
    print(f"\n  Courier {first_name} {last_name} added successfully! (ID: {new_courier.get_courier_id()})")
    return new_courier


def display_all_couriers(couriers: list):
    """
    Displays the full list of all registered couriers with their availability.
    Shows a message if no couriers are registered yet.

    Args:
        couriers (list): The list of all Courier objects.
    """
    display_title("All Registered Couriers")

    if not couriers:
        print("  No couriers registered yet.")
        return

    for index, courier in enumerate(couriers, start=1):
        print(f"\n  --- Courier #{index} ---")
        courier.display_info()
        display_separator()





# PARCEL FUNCTIONS — by Nina


def input_parcel() -> Parcel:
    """
    Prompts the user to enter information for a new parcel
    and returns the created Parcel object.

    Returns:
        Parcel: The newly created Parcel object.
    """
    display_title("Parcel Information")

    description: str = input("  Description  : ").strip()
    while not description:
        print("  Description cannot be empty.")
        description = input("  Description  : ").strip()

    weight_str: str = input("  Weight (kg)  : ").strip()
    while not validate_weight(weight_str):
        print("  Weight must be a positive number (e.g. 2.5).")
        weight_str = input("  Weight (kg)  : ").strip()
    weight: float = float(weight_str)

    print("  Dimensions (in cm):")

    length_str: str = input("  Length : ").strip()
    while not validate_weight(length_str):
        print("  Length must be a positive number.")
        length_str = input("  Length : ").strip()

    width_str: str = input("  Width  : ").strip()
    while not validate_weight(width_str):
        print("  Width must be a positive number.")
        width_str = input("  Width  : ").strip()

    height_str: str = input("  Height : ").strip()
    while not validate_weight(height_str):
        print("  Height must be a positive number.")
        height_str = input("  Height : ").strip()

    dimensions: tuple = (float(length_str), float(width_str), float(height_str))

    fragile_input: str = input("  Fragile? (yes / no) : ").strip().lower()
    fragile: bool = fragile_input in ("yes", "y", "oui", "o")

    new_parcel = Parcel(description, weight, dimensions)
    if fragile:
        new_parcel.mark_as_fragile()

    return new_parcel




# DELIVERY FUNCTIONS — by Hassane


def create_delivery(clients: list, couriers: list, deliveries: list):
    """
    Manages the full process of creating a new delivery.

    Args:
        clients (list): The list of registered clients.
        couriers (list): The list of registered couriers.
        deliveries (list): The existing list of deliveries to update.
    """
    display_title("Create a New Delivery")

    if not clients:
        print("  No clients registered. Please add a client first (option 1).")
        return

    if not couriers:
        print("  No couriers registered. Please add a courier first (option 2).")
        return

    courier = find_available_courier(couriers)
    if not courier:
        print("  No couriers are available right now. Please try again later.")
        return

    print("\n  --- Registered Clients ---")
    for index, client in enumerate(clients, start=1):
        print(f"  {index}. {client.get_first_name()} {client.get_last_name()} (ID: {client.get_client_id()})")

    print()
    choice_str: str = input("  Select a client by number : ").strip()
    while not choice_str.isdigit() or not (1 <= int(choice_str) <= len(clients)):
        print(f"  Please enter a number between 1 and {len(clients)}.")
        choice_str = input("  Select a client by number : ").strip()

    selected_client = clients[int(choice_str) - 1]

    parcel = input_parcel()

    print()
    pickup: str = input("  Pickup address   : ").strip()
    while not pickup:
        print("  Pickup address cannot be empty.")
        pickup = input("  Pickup address   : ").strip()

    drop_off: str = input("  Drop-off address : ").strip()
    while not drop_off:
        print("  Drop-off address cannot be empty.")
        drop_off = input("  Drop-off address : ").strip()

    new_delivery = Delivery(selected_client, courier, parcel, pickup, drop_off)
    total_fee = new_delivery.calculate_total_fee()

    courier.set_availability(False)
    selected_client.add_order(new_delivery.get_delivery_id())
    deliveries.append(new_delivery)
    save_delivery(new_delivery)

    print(f"\n  Delivery created successfully!")
    print(f"  Delivery ID  : {new_delivery.get_delivery_id()}")
    print(f"  Courier      : {courier.get_first_name()} {courier.get_last_name()}")
    print(f"  Total Fee    : {total_fee:,.0f} FCFA")


def track_delivery(deliveries: list):
    """
    Allows the user to search for a delivery by its unique ID
    and displays its current status and full details.

    Args:
        deliveries (list): The list of all Delivery objects.
    """
    display_title("Track a Delivery")

    if not deliveries:
        print("  No deliveries recorded yet.")
        return

    delivery_id: str = input("  Enter Delivery ID : ").strip()
    delivery = find_delivery_by_id(deliveries, delivery_id)

    if delivery:
        delivery.display_details()
    else:
        print(f"  No delivery found with ID: {delivery_id.upper()}")


def update_delivery_status(deliveries: list):
    """
    Allows the user to update the status of an existing delivery.

    Args:
        deliveries (list): The list of all Delivery objects.
    """
    display_title("Update Delivery Status")

    if not deliveries:
        print("  No deliveries recorded yet.")
        return

    delivery_id: str = input("  Enter Delivery ID : ").strip()
    delivery = find_delivery_by_id(deliveries, delivery_id)

    if not delivery:
        print(f"  No delivery found with ID: {delivery_id.upper()}")
        return

    print(f"\n  Current status : {delivery.get_status().upper()}")
    print(f"  Valid statuses : {', '.join(VALID_STATUSES)}")

    new_status: str = input("\n  New status : ").strip().lower()
    while new_status not in VALID_STATUSES:
        print(f"  Invalid status. Choose from : {', '.join(VALID_STATUSES)}")
        new_status = input("  New status : ").strip().lower()

    
    delivery.update_status(new_status)

    # Libérer le livreur quand la livraison est terminée
    if new_status == "delivered":
        delivery.get_courier().set_availability(True)


def display_all_deliveries(deliveries: list):
    """
    Displays a summary of all deliveries with their IDs,
    client names, courier names and current statuses.

    Args:
        deliveries (list): The list of all Delivery objects.
    """
    display_title("All Deliveries")

    if not deliveries:
        print("  No deliveries recorded yet.")
        return

    print(f"  {'ID':<12} {'Client':<22} {'Courier':<22} {'Status':<12} {'Fee (FCFA)'}")
    display_separator()

    for delivery in deliveries:
        client = delivery.get_client()
        courier = delivery.get_courier()
        client_name = f"{client.get_first_name()} {client.get_last_name()}"
        courier_name = f"{courier.get_first_name()} {courier.get_last_name()}"
        print(f"  {delivery.get_delivery_id():<12} {client_name:<22} {courier_name:<22} "
              f"{delivery.get_status():<12} {delivery.get_total_fee():,.0f}")

    display_separator()
    print(f"  Total : {len(deliveries)} delivery(ies)")


def generate_report(deliveries: list):
    """
    Counts deliveries by status, displays the statistics
    and saves the report to a file.

    Args:
        deliveries (list): The list of all Delivery objects.
    """
    display_title("Delivery Report")

    if not deliveries:
        print("  No deliveries to report on yet.")
        return

    status_counts: dict = {
        "pending": 0,
        "in_transit": 0,
        "delivered": 0,
        "cancelled": 0
    }

    total_revenue: float = 0.0

    for delivery in deliveries:
        status = delivery.get_status()
        if status in status_counts:
            status_counts[status] += 1
        total_revenue += delivery.get_total_fee()

    # coded by Nimatou
    print(f"\n  Total deliveries   : {len(deliveries)}")
    display_separator()
    print(f"  Pending            : {status_counts['pending']}")
    print(f"  In Transit         : {status_counts['in_transit']}")
    print(f"  Delivered          : {status_counts['delivered']}")
    print(f"  Cancelled          : {status_counts['cancelled']}")
    display_separator()
    print(f"  Total Revenue      : {total_revenue:,.0f} FCFA")

    save_report(deliveries)
    print(f"\n  Report saved to file successfully.")
