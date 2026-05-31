# =============================================================================
# QuickDeliver_BF — DELIVERY MANAGEMENT SYSTEM
# menu.py — User interaction functions (input handling and display)
# Members Cheick, Ezekiel, Hassane, Nina
# Burkina Institute of Technology 
# =============================================================================


from models import Client, Courier, Parcel, Delivery, VALID_STATUSES
from file_handler import save_delivery, save_report
from utils import (validate_phone, validate_email, validate_weight,
                   display_separator, display_title,
                   find_available_courier, find_delivery_by_id)


# =============================================================================
#                           MAIN MENU by Hassane 
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
    
# CLIENT FUNCTIONS — By Cheick 



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

    # Collect last name — cannot be empty
    last_name: str = input("  Last name    : ").strip()
    while not last_name:
        print("  Last name cannot be empty.")
        last_name = input("  Last name    : ").strip()

    # Collect first name — cannot be empty
    first_name: str = input("  First name   : ").strip()
    while not first_name:
        print("   First name cannot be empty.")
        first_name = input("  First name   : ").strip()

    # Collect and validate phone number (exactly 8 digits)
    phone: str = input("  Phone (8 digits) : ").strip()
    while not validate_phone(phone):
        print("   Phone number must contain exactly 8 digits.")
        phone = input("  Phone (8 digits) : ").strip()

    # Collect and validate email address
    email: str = input("  Email        : ").strip()
    while not validate_email(email):
        print("   Invalid email — must contain '@' and '.'.")
        email = input("  Email        : ").strip()

    # Collect address — cannot be empty
    address: str = input("  Address      : ").strip()
    while not address:
        print("  Address cannot be empty.")
        address = input("  Address      : ").strip()

    # Create and return the new Client object
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

    # Check if the list is empty
    if not clients:
        print("  No clients registered yet.")
        return

    # for loop to display each client's information
    for index, client in enumerate(clients, start=1):
        print(f"\n  --- Client #{index} ---")
        client.display_info()
        display_separator()



 
# COURIER FUNCTIONS — coded by Ezekiel 

def input_courier(courier: list) -> Courier:
    """
    prompts the user to enter information for a new courier 
    and returns the created courier object.

    Args:
    couriers (list): The existing list of couriers.

    Returns
    Courier: The newly created courier object.
    """
    display_title("Add a New courier")

    # Collect last name -cannot be empty
    last_name:str = input("  Last name   : ").strip()
    while not last_name:
        print("Last name cannot be ampty.")
        last_name = input("First name   : ").strip()

        #Collect last name -cannot be empty
        first_name:str = input("  First name   : ").strip()
    while not first_name:
        print("First name cannot be ampty.")
        first_name = input("  First name   : ").strip()
        
        # Collect and validate phone number
        phone:str = input("  Phone(8 digits)   : ").strip()
    while not validate_phone(phone):
        print("Phone number must contain exactly 8 digits.")
        phone = input("   Phone(8 digits)   : ").strip()

        # Collect and validate email address
        email:str = input("  Email   : ").strip()
    while not validate_email(email):
        print("Invalid email -must contain '@' and '.'.")
        last_name = input("First name   : ").strip()

        # Collect vehicle type - connot be empty
    vehicle= input("  Vehicle type (motorbike / car / bicycle) : ").strip()
    while not vehicle:
        print("Vehicle type cannot be ampty.")
        vehicle = input("Vehicle type   : ").strip()

        # Collect delivery zone - connot be empty
        zone: str = input("  Delivery zone : ").strip()
    while not zone:
        print("Delivery zone cannot be ampty.")
        zone = input("Delivery zone   : ").strip()

        # Create and return the new Courier object 
        new_courier = courier(last_name, first_name, phone, email, vehicle, zone)
        print(f"\n Coursier {first_name} {last_name} added!(ID: {new_courier.get_courier_id()})")
        return new_courier

    def display_all_couriers(couriers: list):
        """
        Displays the full list of all registered couriers with their availability.
Shows a message if not coursiers are registered yet

args:
    couriers (list): The list of all coursier objects.
    """
        display_title("All registered couriers")

        # Check if the list is empty
        if not couriers:
         print(" No coursiers registered yet.")
        return
    
    # for loop to display each courier's information
    for index, coursier in enumerate(courier, start=1):
        coursier.display_info()
        # Show availability status explicitly
        status_label = " available" if courier.is_available() else " Unavailable"
        print(f" Status     : {status_label}")
        display_separator()



# PARCEL FUNCTIONS Code by Nina 


def input_parcel() -> Parcel:
    """
    Prompts the user to enter information for a new parcel
    and returns the created Parcel object.

    Returns:
        Parcel: The newly created Parcel object.
    """
    display_title("Parcel Information")

    # Collect description — cannot be empty
    description: str = input("  Description  : ").strip()
    while not description:
        print("   Description cannot be empty.")
        description = input("  Description  : ").strip()

    # Collect and validate weight
    weight_str: str = input("  Weight (kg)  : ").strip()
    while not validate_weight(weight_str):
        print("  Weight must be a positive number (e.g. 2.5).")
        weight_str = input("  Weight (kg)  : ").strip()
    weight: float = float(weight_str)

    # Collect dimensions — each must be a positive number
    print("  Dimensions (in cm):")

    length_str: str = input("Length : ").strip()
    while not validate_weight(length_str):     # reuse positive float check
        print("Length must be a positive number.")
        length_str = input("Length : ").strip()

    width_str: str = input("Width  : ").strip()
    while not validate_weight(width_str):
        print("Width must be a positive number.")
        width_str = input("Width  : ").strip()

    height_str: str = input("Height : ").strip()
    while not validate_weight(height_str):
        print("Height must be a positive number.")
        height_str = input("Height : ").strip()

    # Store dimensions as a tuple (demonstrates tuple usage)
    dimensions: tuple = (float(length_str), float(width_str), float(height_str))

    # Ask if the parcel is fragile
    fragile_input: str = input("Fragile? (yes / no) : ").strip().lower()
    fragile: bool = fragile_input in ("yes", "y", "oui", "o")

    # Create the Parcel object and mark as fragile if needed
    new_parcel = Parcel(description, weight, dimensions)
    if fragile:
        new_parcel.mark_as_fragile()

    return new_parcel




