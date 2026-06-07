# 🛒 Inventory & E-Commerce Management Web App

A full-stack web application built with **Python**, **HTML/CSS**, and **SQL** that supports both **Admin** and **User** logins for managing inventory and processing orders.

---

## 📌 Features

### 👤 User Portal
- 🔐 User Login with Email & Mobile Number
- 🛍️ Browse items in card format (Name, Price, Image, Add to Cart button)
- 🔎 Search bar to filter items by name or keyword
- 🧮 Sorting bar based on category
- 🛒 Cart to add and review items before purchase
- 🧾 Order History with:
  - Last Order
  - Last 5 Orders
  - Total Amount Spent
- 🤖 Chatbot with predefined queries:
  - `last order`
  - `last 5 orders`
  - `total amount spent`

---

### 🛠️ Admin Portal
- 🔐 Admin Login
- 📦 Inventory Management:
  - ➕ **Add Item**: Name, Price, Image URL, Quantity
  - ❌ **Delete Item**: by Item ID
  - 🔄 **Restock Item**: by Item ID and additional Quantity
- 📊 Reports & Insights:
  - 📋 View entire inventory
  - 📦 View total orders
  - 💡 Smart suggestions:
    - Most Ordered Items
    - Least Ordered Items
    - Items with Low Stock

---

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQL (MySQL / PostgreSQL / SQLite)

---

## 📁 Project Structure (Example)

```
project/
│
├── static/                  # CSS, JS, images
├── templates/               # HTML templates
├── app.py                   # Main Flask or Django entry point
├── models.py                # SQLAlchemy / Django ORM models
├── chatbot.py               # Chatbot logic
├── database.db              # SQLite DB (or MySQL/PostgreSQL config)
├── requirements.txt
└── README.md
```

---

## 🧪 Getting Started

### ✅ Prerequisites

- Python 3.x
- pip
- SQL database (SQLite / MySQL / PostgreSQL)

---

### 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/darshanchouthai/InventoryManagement.git
   cd ecommerce-inventory-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database**
   - Update connection in `app.py` or `settings.py` as per your SQL database.

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access**
   - Open browser at `http://localhost:5000/`
---

## 💻 Admin Functionalities Summary

| Action         | Inputs                           | Description                     |
|----------------|----------------------------------|---------------------------------|
| Add Item       | Name, Price, Image URL, Quantity | Adds new item to inventory      |
| Delete Item    | Item ID                          | Removes item from inventory     |
| Restock Item   | Item ID, Quantity                | Increases item stock            |
| View Inventory | –                                | Displays all items              |
| View Orders    | –                                | Displays order history          |
| Suggestions    | –                                | Shows top/least ordered items, low stock |

---

## 👤 User Functionalities Summary

| Feature        | Description                                          |
|----------------|------------------------------------------------------|
| Item Cards     | Visual representation with image, price, add button |
| Cart           | Store items before purchase                         |
| Chatbot        | Handles: last order, last 5 orders, total spent     |
| Sort/Search    | Filter and order items                              |
| Order History  | View previous purchases                             |
| Login Info     | Email and mobile stored                             |

---

## ✅ Future Enhancements

- Email confirmations for orders
- Stock alert notifications
- Profile management for users
- Export reports for admin

---

## 🧑‍💻 Author

Developed by **Your Name**  
📧 your.email@example.com  
🌐 [GitHub](https://github.com/darshanchouthai)

---

## 📄 License

This project is licensed under the MIT License.
