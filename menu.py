# =============================================================================
# QuickDeliver_BF — DELIVERY MANAGEMENT SYSTEM
# menu.py — User interaction functions (input handling and display)
# Members Cheick, Ezekiel, Hassane, Nina , Nimatou
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







# DELIVERY FUNCTIONS — Hassane

def create_delivery(clients: list, couriers: list, deliveries: list):
    """
    Manages the full process of creating a new delivery :
    - Checks that clients and couriers exist
    - Finds an available courier automatically
    - Collects parcel information
    - Creates the Delivery object
    - Calculates the total fee
    - Updates courier availability
    - Updates client order history
    - Saves the delivery to file

    Args:
        clients (list): The list of registered clients.
        couriers (list): The list of registered couriers.
        deliveries (list): The existing list of deliveries to update.
    """
    display_title("Create a New Delivery")

    # Check that at least one client exists
    if not clients:
        print(" No clients registered. Please add a client first (option 1).")
        return

    # Check that at least one courier exists
    if not couriers:
        print(" No couriers registered. Please add a courier first (option 2).")
        return

    # Find the first available courier automatically
    courier = find_available_courier(couriers)
    if not courier:
        print(" No couriers are available right now. Please try again later.")
        return

    # Display all clients for the user to choose from
    print("\n  --- Registered Clients ---")
    for index, client in enumerate(clients, start=1):
        print(f"  {index}. {client.get_first_name()} {client.get_last_name()} (ID: {client.get_client_id()})")

    # Ask user to select a client by number
    print()
    choice_str: str = input("  Select a client by number : ").strip()
    while not choice_str.isdigit() or not (1 <= int(choice_str) <= len(clients)):
        print(f" Please enter a number between 1 and {len(clients)}.")
        choice_str = input("  Select a client by number : ").strip()

    # Retrieve selected client (list index is choice - 1)
    selected_client = clients[int(choice_str) - 1]

    # Collect parcel details
    parcel = input_parcel()

    # Collect pickup and drop-off addresses
    print()
    pickup: str = input("  Pickup address   : ").strip()
    while not pickup:
        print(" Pickup address cannot be empty.")
        pickup = input("  Pickup address   : ").strip()

    drop_off: str = input("  Drop-off address : ").strip()
    while not drop_off:
        print(" Drop-off address cannot be empty.")
        drop_off = input("  Drop-off address : ").strip()

    # Create the Delivery object
    new_delivery = Delivery(selected_client, courier, parcel, pickup, drop_off)

    # Calculate and store the total shipping fee
    total_fee = new_delivery.calculate_total_fee()

    # Mark the assigned courier as unavailable
    courier.set_availability(False)

    # Add delivery ID to the client's order history
    selected_client.add_order(new_delivery.get_delivery_id())

    # Add the delivery to the in-memory list
    deliveries.append(new_delivery)

    # Save the delivery to file
    save_delivery(new_delivery)

    # Confirmation message
    print(f"\n Delivery created successfully!")
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

    # Ask for the delivery ID
    delivery_id: str = input("  Enter Delivery ID : ").strip()

    # Search for the delivery using the utility function
    delivery = find_delivery_by_id(deliveries, delivery_id)

    if delivery:
        delivery.display_details()
    else:
        print(f" No delivery found with ID: {delivery_id.upper()}")


def update_delivery_status(deliveries: list):
    """
    Allows the user to update the status of an existing delivery.
    Displays the valid status options and validates the user's input.

    Args:
        deliveries (list): The list of all Delivery objects.
    """
    display_title("Update Delivery Status")

    if not deliveries:
        print("  No deliveries recorded yet.")
        return

    # Ask for the delivery ID to update
    delivery_id: str = input("  Enter Delivery ID : ").strip()
    delivery = find_delivery_by_id(deliveries, delivery_id)

    if not delivery:
        print(f" No delivery found with ID: {delivery_id.upper()}")
        return

    # Show current status and valid options
    print(f"\n  Current status : {delivery.get_status().upper()}")
    print(f"  Valid statuses : {', '.join(VALID_STATUSES)}")

    # Collect and validate the new status
    new_status: str = input("\n  New status : ").strip().lower()
    while new_status not in VALID_STATUSES:
        print(f" Invalid status. Choose from : {', '.join(VALID_STATUSES)}")
        new_status = input("  New status : ").strip().lower()

    # Apply the status update
    delivery.update_status(new_status)

    # If the delivery is marked as delivered, use the dedicated method
    if new_status == "delivered":
        delivery.mark_as_delivered()
        # Free up the courier when delivery is completed
        delivery.get_courier().set_availability(True)


def display_all_deliveries(deliveries: list):
    """
    displays a summary of all deliveries with their IDs,
    client names, courier names and current statuses.
    Shows a message if no deliveries exist yet

    Args:
        deliveries (list): The list of all Delivery objects.
    """
    display_title("All deliveries")

    if not deliveries:
        print("  No deliveries recorded yet.")
        return

    # Table header
    print(f"  {'ID':<12} {'Client':<22} {'Courier':<22} {'Status':<12} {'Fee (FCFA)'}")
    display_separator()

    # for loop to display a summary row for each delivery
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
    Counts deliveries by status using a dictionary,
    displays the statistics in the terminal,
    and saves the report to a file.

    Args:
        deliveries (list): the list of all Delivery objects.
    """
    display_title("delivery Report")

    if not deliveries:
        print("  No deliveries to report on yet.")
        return

    # Use a dictionary to count deliveries by status ---
    status_counts: dict = {
        "pending": 0,
        "in_transit": 0,
        "delivered": 0,
        "cancelled": 0
    }

    total_revenue: float = 0.0

    # for loop to tally each delivery's status and add up revenue
    for delivery in deliveries:
        status = delivery.get_status()
        if status in status_counts:
            status_counts[status] += 1
        total_revenue += delivery.get_total_fee()
    #coded by Nimatou
    # Display the statistics in the terminal
    print(f"\n  Total deliveries   : {len(deliveries)}")
    display_separator()
    print(f"  Pending            : {status_counts['pending']}")
    print(f"  In Transit         : {status_counts['in_transit']}")
    print(f"  Delivered          : {status_counts['delivered']}")
    print(f"  Cancelled          : {status_counts['cancelled']}")
    display_separator()
    print(f"  Total Revenue      : {total_revenue:,.0f} FCFA")

    # Save the report to file using the file_handler function
    save_report(deliveries)
    print(f"\n Report saved to file successfully.")
  




