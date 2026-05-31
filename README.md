# QuickDeliver_BF
A python console application  to manage deliveries, client, couriers and parcels for small transport business

# 🚚 QuickDeliver_BF

> A Python console application built as part of the Programming I with Python course.
> by first year students in computer-science of Burkina Institute of Technology (BIT) — May 2026.

---

## 📌 Description

QuickDeliver_BF is a console-based delivery management application built in Python.
It allows a transport company to register clients and couriers, create and track deliveries,
calculate shipping fees automatically, and generate activity reports — all saved to local
text files for data persistence.

The application runs entirely in the terminal. The user navigates through a numbered menu
and interacts by typing numbers and text.

---

##  How to Run the Project

### Requirements
- Python **3.10** or higher
- No external libraries required — only built-in Python modules are used

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/hassane-labs/QuickDeliver_bf.git
```

2. **Move into the project folder**
```bash
cd QuickDeliver_bf
```

3. **Run the program**
```bash
python main.py
```

> ⚠️ Use `python3` instead of `python`.

---

## Features

- Register a new client with their personal information
- Register a new courier with their vehicle type and delivery zone
- Create a delivery by linking a client, a courier and a parcel
- Automatically calculate shipping fees based on parcel weight
- Apply a 20% surcharge for fragile parcels
- Track any delivery status using its unique ID
- Update a delivery status : `pending → in transit → delivered / cancelled`
- View the full list of clients, couriers and deliveries
- Generate a statistical report saved automatically to a text file
- Persist all delivery data across sessions using local text files

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Main programming language |
| `datetime` | Built-in | Creation and delivery timestamps |
| `uuid` | Built-in | Automatic unique ID generation |
| `os` | Built-in | File system management |

---

## 📁 Project Structure

```
QuickDeliver_BF/
│
├── main.py           → Entry point — launches the app and runs the main menu loop
├── models.py         → All classes : Person, Client, Courier, Parcel, Delivery
├── menu.py           → User interaction functions (input handling, display)
├── file_handler.py   → File read and write functions
├── utils.py          → Utility functions (validation, search, formatting)
│
├── deliveries.txt    → Auto-generated — stores all delivery records
├── report.txt        → Auto-generated — statistical report of all deliveries
│
└── README.md         → Project documentation
```

> 💡 The `.txt` files are created automatically by the program the first time
> data is saved. You do not need to create them manually.
---

## 🧱 OOP Structure

### `Person` — Parent Class
Represents any person in the system with their basic personal information.
- **Attributes :** `_last_name`, `_first_name`, `_phone`, `_email`
- **Key methods :** `get_last_name()`, `get_first_name()`, `display_info()`, `__str__()`
- **Inheritance :** None — this is the root class

---

### `Client` — Inherits from `Person`
Represents a client who places delivery orders.
- **Additional attributes :** `_address`, `_client_id`, `_order_history`
- **Key methods :** `add_order()`, `display_order_history()`, `display_info()`
- **Inheritance :** extends `Person`

---

### `Courier` — Inherits from `Person`
Represents a courier who transports parcels.
- **Additional attributes :** `_vehicle`, `_zone`, `_courier_id`, `_available`, `_completed_deliveries`
- **Key methods :** `is_available()`, `set_availability()`, `add_delivery()`, `display_info()`
- **Inheritance :** extends `Person`

---

### `Parcel`
Represents a parcel to be delivered with its physical characteristics.
- **Attributes :** `_parcel_id`, `_description`, `_weight`, `_dimensions`, `_fragile`, `_creation_date`
- **Key methods :** `calculate_volume()`, `calculate_base_fee()`, `mark_as_fragile()`
- **Inheritance :** None

---

### `Delivery`
Represents a complete delivery — links a Client, a Courier and a Parcel together.
- **Attributes :** `_delivery_id`, `_client`, `_courier`, `_parcel`, `_status`, `_creation_date`, `_delivery_date`, `_total_fee`
- **Key methods :** `update_status()`, `mark_as_delivered()`, `calculate_total_fee()`, `display_details()`
- **Inheritance :** None

---

### The 4 OOP Principles in QuickDeliver_BF

| Principle | Where it appears in the code |
|---|---|
| **Encapsulation** | All attributes are private (`_weight`, `_phone`...) and only accessible via getters and setters |
| **Inheritance** | `Client` and `Courier` both inherit from `Person` using `super().__init__()` |
| **Polymorphism** | `display_info()` behaves differently in `Person`, `Client` and `Courier` |
| **Abstraction** | `create_delivery()` hides all internal complexity behind a single clean function call |

---
## 👥 Group Members

| Name | Role | Files | GitHub Profile |
|---|---|---|---|
| KABORÉ Gueswendé Hassane | Tech Lead — Menu, Main, GitHub, README | `main.py` · `menu.py` | [@hassane-labs](https://github.com/hassane-labs) |
| DA Gloire Jeanine | File Handling — Save, Load, Report | `file_handler.py` | [@dajeanine79-hash](https://github.com/dajeanine79-hash) |
| HOYNOUMA Nimatou | Person Class · Utilities · Report Stats | `models.py` · `utils.py` · `menu.py` | [@nimatouhoynouma00-commits](https://github.com/nimatouhoynouma00-commits) |
| KABORE Wendso Ezekiel | Courier Class · Courier Input & Display | `models.py` · `menu.py` | [@Wendso-226](https://github.com/Wendso-226 ) |
| KIENDREBEOGO Nina | Parcel Class · Delivery Class · Search Utils · Parcel Input | `models.py` · `utils.py` · `menu.py` | [@ninakiendrebeogo171-bot](https://github.com/ninakiendrebeogo171-bot) |
| GUISSOU Cheick Faissale| Client Class · Client Input & Display | `models.py` · `menu.py` | [@KEUCH226](https://github.com/KEUCH226) |

---

## 🙏 Acknowledgements

- **Ms. Kweyakie Afi Blebo** — for teaching and guidance throughout the module
- Official Python documentation : [https://docs.python.org/3/](https://docs.python.org/3/)
- [How To Write a USEFUL README On Github](https://youtu.be/E6NO0rgFub4?si=nxLjKfAzaXOC-Hwa)
- [ POO Python de Zéro en 2026 : Formation complète 1h (encapsulation, héritage, polymorphisme, ...)](https://youtu.be/QIraKuaHPQ8?si=RapxDTw8-zAZPKS6)
- [📱Comment Créer une Application Mobile avec 🐍Python](https://youtu.be/W1x4EmfeXGg?si=G6CRyZho1Vo1v7xx)
---

*Burkina Institute of Technology — CS28 — GROUP 05*




