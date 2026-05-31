#QuickDeliver_BF — DELIVERY MANAGEMENT SYSTEM
#Module — file_handler.py
#file_handler.py goal — File read and write functions
#coded by Jeanine


import datetime
    #import datetime — Import the modulus datetime that permit to manipulate the dates and hours from python standard library 

from models import Delivery
    #from models import Delivery — import the class delevery from the file model.py


#DELIVERIES_FILE and REPORT_FILE — contain constants 

DELIVERIES_FILE = "deliveries.txt"
    #deliveries.txt: file that contains all the deliveries

REPORT_FILE = "report.txt"
    #report.txt: file that contains the last static report generated


#FILE FUNCTIONS

    #recording of a delivery to the deliveries.txt file  
    
def save_delivery(delivery: Delivery):
    #def save_delivery(delivery: Delivery):a function that takes an object delivery in parameter and return nothing
     
    with open(DELIVERIES_FILE, "a", encoding="utf-8") as file:
        #with: permits to close automatically the file
        #mode'a'(append): that means add, preserves existing data
        #encoding="utf-8": supports accented characters
        #open in mode append:can creates the file automatically if it did not exist.
        
        
        file.write(delivery.to_file_string() + "\n")
        #convert a delivery to a formatted string via (to_file_string()) and write the line in the file adding a newline


def load_deliveries() -> list:
    #charge all the deliveries in the file deliveries.txt  
    #Returns:
        #list: A list of non empty string lines from the file.
        #an empty list if the file does not exist yet.
    
    try:
        # Try to open and read the file with mode 'r'
        
        with open(DELIVERIES_FILE, "r", encoding="utf-8") as file:
            # try to open the DELIVERIES-FILE in UTF-8 read mode and access it via the file variable.The with statement ensure the file closes automatically at the end.
            
            lines = [line.strip() for line in file.readlines()]
                #readlines()- read all les lines
                #strip()- to each lines delete spacings et lines breaks
            
            return [line for line in lines if line]
                # Filter out any empty lines that may exist and return only non empty lines
    
    except FileNotFoundError:
        return []
         # File does not exist yet — return an empty list


def save_report(deliveries: list):
    """
    Generates a full statistical report from the deliveries list
    and saves it to the report text file.

    The report includes :
    - Total number of deliveries
    - Number of deliveries per status
    - Total revenue generated in FCFA

    Args:
        deliveries (list): The list of all Delivery objects.
    """
    
    status_counts: dict = {
        "pending": 0,
        "in_transit": 0,
        "delivered": 0,
        "cancelled": 0
    }
      # Counting dictionary initialized to zero for each possible statut 

    total_revenue: float = 0.0
    #variable of type float that accumulates total revenue initialized to 0  

    for delivery in deliveries:
        # for loop to go through every delivery and tally up counts and revenue
      
        status = delivery.get_status()
          #retrieving the status via get_status
      
        if status in status_counts:
            status_counts[status] += 1
            # Increment the count for this status if it exists in the dictionary
          
        total_revenue += delivery.get_total_fee()
            # Add this delivery's fee to the total revenue

    # --- Write the report to file ---
  
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
       # Open in write mode ("w") so the report is always fresh
      
        # Report header
        file.write("=" * 60 + "\n")
        file.write("   QuickDelivery_BF — DELIVERY REPORT\n")
        file.write(f"   Generated on : {datetime.datetime.now().strftime('%d/%m/%Y at %H:%M')}\n")
        file.write("=" * 60 + "\n\n")

        # Total number of deliveries
        file.write(f"  Total deliveries   : {len(deliveries)}\n\n")

        # Breakdown by status
        file.write("  --- BREAKDOWN BY STATUS ---\n")
        file.write(f"  Pending            : {status_counts['pending']}\n")
        file.write(f"  In Transit         : {status_counts['in_transit']}\n")
        file.write(f"  Delivered          : {status_counts['delivered']}\n")
        file.write(f"  Cancelled          : {status_counts['cancelled']}\n\n")

        # Total revenue
        file.write("  --- REVENUE ---\n")
        file.write(f"  Total Revenue      : {total_revenue:,.0f} FCFA\n\n")

        #footer
        file.write("=" * 60 + "\n")
        file.write("   End of report\n")
        file.write("=" * 60 + "\n")


