# **Basil Energetics Private Ltd - Price Calculator**  

## **Project Overview**  
This project is a **Solar Energy Price Calculator** for **Basil Energetics Private Ltd**. It enables users to calculate solar panel requirements, rooftop area, PV panel rating, and overall cost based on the electrical appliances and their quantities. The app also saves customer details and appliance data to a MySQL database for record-keeping.

---

## **Features**  
- Calculate solar panel requirements and costs.  
- Interactive and user-friendly interface using Streamlit.  
- Save customer and appliance data to a MySQL database.  
- Display results dynamically and aesthetically.

---

## **Requirements**  

### **Software Prerequisites**  
- Python (3.8 or above)  
- MySQL Server  
- Streamlit (Python package)

### **Python Libraries**  
Install the required Python libraries using the following command:  
```bash
pip install streamlit mysql-connector-python
```

---

## **Setting Up the Database**  

### **Step 1: Create the Database**
1. Open MySQL Workbench or the MySQL CLI.
2. Run the following SQL commands to create the database and table:
```sql
CREATE DATABASE basil_energetics;

USE basil_energetics;

CREATE TABLE sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_phone VARCHAR(15),
    salesman_name VARCHAR(100),
    qty_1_ton_ac INT,
    qty_1_5_ton_ac INT,
    qty_50l_fridge INT,
    qty_180l_fridge INT,
    qty_300l_fridge INT,
    qty_ceiling_fan INT,
    qty_tube_light INT,
    qty_7w_bulb INT,
    qty_9w_bulb INT,
    qty_12w_bulb INT,
    qty_15w_street_light INT,
    qty_24w_street_light INT,
    qty_other_loads INT
);
```

### **Step 2: Configure Database Access**  
Before running the application, ensure to configure your MySQL credentials in the `app.py` file.  

- Open the `app.py` file in any code editor.  
- Replace the placeholders `<YOUR_HOST>`, `<YOUR_USER>`, and `<YOUR_PASSWORD>` in the database connection code with your MySQL details.  

For example:  
```python
conn = mysql.connector.connect(
    host="<YOUR_HOST>",
    user="<YOUR_USER>",
    password="<YOUR_PASSWORD>",
    database="basil_energetics"
)
```
## **Running the Application**

### **Step 1: Place the Logo**
- Save your company logo at `BEPL_picture.jpg`.

### **Step 2: Launch the App**
Run the following command in the terminal:  
```bash
streamlit run app.py
```

---

## **Using the Application**

1. **Fill Customer Details**:  
   Enter the customer name, phone number, and salesman name.  

2. **Input Appliance Quantities**:  
   Provide the quantities of appliances.  

3. **Click "Calculate"**:  
   View the solar panel requirements, rooftop area, and total cost.  

4. **Save to Database**:  
   Click "Load to Database" to store the data in MySQL.

---

## **Viewing Saved Data**  

### **Step 1: Access MySQL**
Log into your MySQL server using Workbench or CLI.

### **Step 2: Query Data**
Run the following command to view saved data:  
```sql
USE basil_energetics;
SELECT * FROM sales_data;
```

---

## **Project Structure**

```plaintext
.
├── app.py                # Main Streamlit app file
├── BEPL_picture.jpg      # Company logo file
├── README.md             # Project documentation
```

---

## **Author**  
- **Name**: Vishnuprasaath M  
- **Contact**: [LinkedIn Profile](https://www.linkedin.com/in/vishnuprasaath-m-0298a0287)

---

## **License**  
This project is licensed under **Basil Energetics Pvt Ltd**. Unauthorized use or modification without permission is prohibited.

---
