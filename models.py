# =============================================================================
# QUICKDELIVER_BF — DELIVERY MANAGEMENT SYSTEM
# models.py — All classes : Person, Client, Courier, Parcel, Delivery
# Burkina Institute of Technology
# =============================================================================

import datetime
import uuid

VALID_STATUSES = ("pending", "in_transit", "delivered", "cancelled")
BASE_RATE_PER_KG: float = 500.0     # FCFA per kilogram
MINIMUM_FEE: float = 1000.0         # Minimum shipping fee in FCFA
FRAGILE_SURCHARGE: float = 0.20     # 20% surcharge for fragile parcels



# PARENT CLASS — Person
# Coded by : Nimatou


class Person:
    """
    Parent class representing a person in the QuickDeliver_BF system.
    Serves as the base class for Client and Courier.
    Demonstrates : Encapsulation (private attributes) and Abstraction.
    """

    # CORRECTION : le nom de la méthode était "_init_" (un seul underscore)
    # au lieu de "__init__" (double underscore). Python ne reconnaissait pas
    # le constructeur, ce qui provoquait une SyntaxError au démarrage.
    def __init__(self, last_name: str, first_name: str, phone: str, email: str):
        """
        Initialises a person with their basic personal information.

        Args:
            last_name (str): The person's last name.
            first_name (str): The person's first name.
            phone (str): The person's phone number.
            email (str): The person's email address.
        """
        # Private attributes — encapsulation
        self._last_name: str = last_name
        self._first_name: str = first_name
        self._phone: str = phone
        self._email: str = email

    # Getters

    def get_last_name(self) -> str:
        """Returns the last name of the person."""
        return self._last_name

    def get_first_name(self) -> str:
        """Returns the first name of the person."""
        return self._first_name

    def get_phone(self) -> str:
        """Returns the phone number of the person."""
        return self._phone

    def get_email(self) -> str:
        """Returns the email address of the person."""
        return self._email

    # Setters 

    def set_phone(self, phone: str):
        """
        Updates the phone number of the person.

        Args:
            phone (str): The new phone number.
        """
        if phone.strip():   # check that the value is not empty
            self._phone = phone

    def set_email(self, email: str):
        """
        Updates the email address of the person.

        Args:
            email (str): The new email address.
        """
        if email.strip():   # check that the value is not empty
            self._email = email

    def display_info(self):
        """
        Displays the basic information of the person.
        This method is overridden in child classes (polymorphism).
        """
        print(f"  Name    : {self._first_name} {self._last_name}")
        print(f"  Phone   : {self._phone}")
        print(f"  Email   : {self._email}")

    def __str__(self) -> str:
        """Returns a short string representation of the person."""
        return f"{self._first_name} {self._last_name} — {self._phone}"



# CHILD CLASS : Client
# Coded by : Cheick
# Inherits from : Person


class Client(Person):
    """
    Represents a client who sends or receives parcels.
    Inherits from Person — demonstrates Inheritance and Polymorphism.
    """

    def __init__(self, last_name: str, first_name: str, phone: str,
                 email: str, address: str):
        """
        Initialises a client with personal information and physical address.

        Args:
            last_name (str): The client's last name.
            first_name (str): The client's first name.
            phone (str): The client's phone number.
            email (str): The client's email address.
            address (str): The client's physical address.
        """
        # Call the parent constructor — inheritance
        super().__init__(last_name, first_name, phone, email)

        # Client-specific private attributes
        self._address: str = address
        self._client_id: str = str(uuid.uuid4())[:8].upper()   # auto-generated unique ID
        self._order_history: list = []                          # list of delivery IDs

    # Getters

    def get_client_id(self) -> str:
        """Returns the unique identifier of the client."""
        return self._client_id

    def get_address(self) -> str:
        """Returns the physical address of the client."""
        return self._address

    def get_order_history(self) -> list:
        """Returns the list of delivery IDs from past orders."""
        return self._order_history

    # Methods

    def add_order(self, delivery_id: str):
        """
        Adds a delivery ID to the client's order history.

        Args:
            delivery_id (str): The unique ID of the delivery to record.
        """
        self._order_history.append(delivery_id)

    def display_info(self):
        """
        Displays the full information of the client.
        Overrides Person.display_info() — demonstrates Polymorphism.
        """
        print(f"  Client ID   : {self._client_id}")
        print(f"  Name        : {self._first_name} {self._last_name}")
        print(f"  Phone       : {self._phone}")
        print(f"  Email       : {self._email}")
        print(f"  Address     : {self._address}")
        print(f"  Orders      : {len(self._order_history)}")

    def display_order_history(self):
        """Displays all past delivery IDs associated with this client."""
        if not self._order_history:
            print("  No orders found for this client.")
        else:
            print(f"  Order history for {self._first_name} {self._last_name}:")
            # for loop to go through each past order
            for index, delivery_id in enumerate(self._order_history, start=1):
                print(f"    {index}. Delivery ID : {delivery_id}")

    def __str__(self) -> str:
        """Returns a short string representation of the client."""
        return f"[CLIENT] {self._first_name} {self._last_name} (ID: {self._client_id})"




# CHILD CLASS : Courier
# Coded by : Ezekiel
# Inherits from : Person

class Courier(Person):
    """
    Represents a courier who transports parcels.
    Inherits from Person — demonstrates Inheritance and Polymorphism.
    """

    def __init__(self, last_name: str, first_name: str, phone: str,
                 email: str, vehicle: str, zone: str):
        """
        Initialises a courier with personal and professional information.

        Args:
            last_name (str): The courier's last name.
            first_name (str): The courier's first name.
            phone (str): The courier's phone number.
            email (str): The courier's email address.
            vehicle (str): Vehicle type (motorbike, car, bicycle...).
            zone (str): The geographical delivery zone.
        """
        # Call the parent constructor — inheritance
        super().__init__(last_name, first_name, phone, email)

        # Courier-specific private attributes
        self._vehicle: str = vehicle
        self._zone: str = zone
        self._courier_id: str = str(uuid.uuid4())[:8].upper()  # auto-generated unique ID
        self._completed_deliveries: list = []                   # list of delivery IDs
        self._available: bool = True                            # available by default

    # Getters

    def get_courier_id(self) -> str:
        """Returns the unique identifier of the courier."""
        return self._courier_id

    def get_vehicle(self) -> str:
        """Returns the vehicle type used by the courier."""
        return self._vehicle

    def get_zone(self) -> str:
        """Returns the delivery zone of the courier."""
        return self._zone

    def is_available(self) -> bool:
        """Returns True if the courier is available, False otherwise."""
        return self._available

    # Setters 

    def set_availability(self, available: bool):
        """
        Updates the availability status of the courier.

        Args:
            available (bool): True if available, False if busy.
        """
        self._available = available

    #  Methods 

    def add_delivery(self, delivery_id: str):
        """
        Records a completed delivery in the courier's history.

        Args:
            delivery_id (str): The unique ID of the completed delivery.
        """
        self._completed_deliveries.append(delivery_id)

    def display_info(self):
        """
        Displays the full information of the courier.
        Overrides Person.display_info() — demonstrates Polymorphism.
        """
        status = "Available" if self._available else "Busy"

        print(f"  Courier ID  : {self._courier_id}")
        print(f"  Name        : {self._first_name} {self._last_name}")
        print(f"  Phone       : {self._phone}")
        print(f"  Email       : {self._email}")
        print(f"  Vehicle     : {self._vehicle}")
        print(f"  Zone        : {self._zone}")
        print(f"  Status      : {status}")
        print(f"  Deliveries  : {len(self._completed_deliveries)}")

    def display_completed_deliveries(self):
        """Displays all delivery IDs completed by this courier."""
        if not self._completed_deliveries:
            print("  No deliveries completed yet.")
        else:
            print(f"  Deliveries by {self._first_name} {self._last_name}:")
            for index, delivery_id in enumerate(self._completed_deliveries, start=1):
                print(f"    {index}. Delivery ID : {delivery_id}")

    def __str__(self) -> str:
        """Returns a short string representation of the courier."""
        availability = "Available" if self._available else "Busy"
        return f"[COURIER] {self._first_name} {self._last_name} — {self._zone} — {availability}"



        

# PARCEL CLASS
# Coded by : Nina
class Parcel:
    """
    Represents a parcel to be delivered with its physical characteristics.
    Demonstrates : Encapsulation and Abstraction.
    """

    def __init__(self, description: str, weight: float, dimensions: tuple):
        """
        Initialises a parcel with description, weight and dimensions.

        Args:
            description (str): Description of the parcel contents.
            weight (float): Weight of the parcel in kilograms.
            dimensions (tuple): Dimensions as (length, width, height) in cm.
        """
        # Private attributes — encapsulation
        self._parcel_id: str = str(uuid.uuid4())[:8].upper()   # auto-generated unique ID
        self._description: str = description
        self._weight: float = weight
        self._dimensions: tuple = dimensions                    # (length, width, height) in cm
        self._fragile: bool = False                             # not fragile by default
        self._creation_date: datetime.date = datetime.date.today()

    #  Getters 

    def get_parcel_id(self) -> str:
        """Returns the unique identifier of the parcel."""
        return self._parcel_id

    def get_weight(self) -> float:
        """Returns the weight of the parcel in kilograms."""
        return self._weight

    def get_dimensions(self) -> tuple:
        """Returns the dimensions of the parcel as a (length, width, height) tuple."""
        return self._dimensions

    def get_description(self) -> str:
        """Returns the description of the parcel contents."""
        return self._description

    def is_fragile(self) -> bool:
        """Returns True if the parcel is marked as fragile, False otherwise."""
        return self._fragile

    # Methods 

    def mark_as_fragile(self):
        """Marks the parcel as fragile — a 20% surcharge will be applied."""
        self._fragile = True

    def calculate_volume(self) -> float:
        """
        Calculates the volume of the parcel from its dimensions tuple.

        Returns:
            float: Volume in cm³ (length x width x height).
        """
        length, width, height = self._dimensions
        return length * width * height

    def calculate_base_fee(self) -> float:
        """
        Calculates the base shipping fee based on parcel weight.
        Rate is 500 FCFA per kg with a minimum of 1000 FCFA.

        Returns:
            float: Base fee in FCFA.
        """
        return max(MINIMUM_FEE, self._weight * BASE_RATE_PER_KG)

    def display_info(self):
        """Displays all physical information about the parcel."""
        fragile_label = "Yes" if self._fragile else "No"
        print(f"  Parcel ID   : {self._parcel_id}")
        print(f"  Description : {self._description}")
        print(f"  Weight      : {self._weight} kg")
        print(f"  Dimensions  : {self._dimensions[0]}cm x {self._dimensions[1]}cm x {self._dimensions[2]}cm")
        print(f"  Volume      : {self.calculate_volume()} cm³")
        print(f"  Fragile     : {fragile_label}")
        print(f"  Created on  : {self._creation_date}")

    def __str__(self) -> str:
        """Returns a short string representation of the parcel."""
        return f"[PARCEL] {self._parcel_id} — {self._description} — {self._weight}kg"




# DELIVERY CLASS
# Coded by : Nina

class Delivery:
    """
    Represents a complete delivery linking a Client, a Courier and a Parcel.
    Manages the full lifecycle from creation to completion.
    Demonstrates : Abstraction — complex logic hidden behind clean methods.
    """

    def __init__(self, client: Client, courier: Courier, parcel: Parcel,
                 pickup_address: str, drop_address: str):
        """
        Initialises a delivery with all associated objects and addresses.

        Args:
            client (Client): The client placing the order.
            courier (Courier): The courier assigned to this delivery.
            parcel (Parcel): The parcel to be delivered.
            pickup_address (str): The address where the parcel is collected.
            drop_address (str): The address where the parcel is delivered.
        """
        # Auto-generated unique ID
        self._delivery_id: str = str(uuid.uuid4())[:8].upper()

        # Linked objects
        self._client: Client = client
        self._courier: Courier = courier
        self._parcel: Parcel = parcel

        # Addresses
        self._pickup_address: str = pickup_address
        self._drop_address: str = drop_address

        # Status starts as "pending" — first value of the VALID_STATUSES tuple
        self._status: str = VALID_STATUSES[0]

        # Dates
        self._creation_date: datetime.datetime = datetime.datetime.now()
        self._delivery_date = None  # set only when marked as delivered

        # Fee calculated later
        self._total_fee: float = 0.0

    #  Getters 

    def get_delivery_id(self) -> str:
        """Returns the unique identifier of the delivery."""
        return self._delivery_id

    def get_status(self) -> str:
        """Returns the current status of the delivery."""
        return self._status

    def get_total_fee(self) -> float:
        """Returns the total shipping fee for this delivery."""
        return self._total_fee

    def get_client(self) -> Client:
        """Returns the client associated with this delivery."""
        return self._client

    def get_courier(self) -> Courier:
        """Returns the courier assigned to this delivery."""
        return self._courier

    def get_parcel(self) -> Parcel:
        """Returns the parcel associated with this delivery."""
        return self._parcel

    #  Methods

    def update_status(self, new_status: str):
        """
        Updates the delivery status if the new value is valid.

        Args:
            new_status (str): Must be one of VALID_STATUSES.
        """
        if new_status in VALID_STATUSES:
            self._status = new_status
        
            if new_status == "delivered":
                self._delivery_date = datetime.datetime.now()
            print(f"  Status updated to : {new_status}")
        else:
            print(f"  Invalid status. Choose from : {VALID_STATUSES}")

    def mark_as_delivered(self):
        """Marks the delivery as delivered and records the exact delivery date and time."""
        self._status = "delivered"
        self._delivery_date = datetime.datetime.now()
        print(f"  Delivery {self._delivery_id} marked as delivered.")

    def calculate_total_fee(self) -> float:
        """
        Calculates the total fee based on parcel weight.
        Adds a 20% surcharge if the parcel is fragile.

        Returns:
            float: Total fee in FCFA.
        """
        base_fee: float = self._parcel.calculate_base_fee()

        # Apply fragile surcharge if needed
        if self._parcel.is_fragile():
            total = base_fee * (1 + FRAGILE_SURCHARGE)  # +20%
        else:
            total = base_fee

        self._total_fee = total
        return self._total_fee

    def display_details(self):
        """Displays the full details of the delivery — client, courier, parcel, status and fee."""
        print(f"\n  {'='*45}")
        print(f"  DELIVERY ID  : {self._delivery_id}")
        print(f"  Status       : {self._status.upper()}")
        print(f"  Created      : {self._creation_date.strftime('%d/%m/%Y %H:%M')}")

        if self._delivery_date:
            print(f"  Delivered    : {self._delivery_date.strftime('%d/%m/%Y %H:%M')}")

        print(f"\n  --- CLIENT ---")
        self._client.display_info()

        print(f"\n  --- COURIER ---")
        self._courier.display_info()

        print(f"\n  --- PARCEL ---")
        self._parcel.display_info()

        print(f"\n  --- ADDRESSES ---")
        print(f"  Pickup       : {self._pickup_address}")
        print(f"  Drop-off     : {self._drop_address}")

        print(f"\n  --- FEE ---")
        print(f"  Total Fee    : {self._total_fee:,.0f} FCFA")
        print(f"  {'='*45}\n")

    def to_file_string(self) -> str:
        """
        Formats the delivery as a pipe-separated string for file storage.

        Returns:
            str: A single line representing this delivery.
        """
        return (f"{self._delivery_id}|"
                f"{self._creation_date.strftime('%d/%m/%Y %H:%M')}|"
                f"{self._client.get_first_name()} {self._client.get_last_name()}|"
                f"{self._courier.get_first_name()} {self._courier.get_last_name()}|"
                f"{self._parcel.get_description()}|"
                f"{self._status}|"
                f"{self._total_fee:.0f} FCFA")

    def __str__(self) -> str:
        """Returns a short string representation of the delivery."""
        return (f"[DELIVERY] {self._delivery_id} — "
             
