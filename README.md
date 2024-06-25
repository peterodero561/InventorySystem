# Inventory System

## 1. Form that is filled by person taking Invetory
![form image](https://github.com/peterodero561/InventorySystem/blob/main/images/form.png)

## 2. Table that is display the contents of the Inventory
![table image](https://github.com/peterodero561/InventorySystem/blob/main/images/table.png)

## 3. Database to store the records inserted in the Inventory
![mysql image](https://github.com/peterodero561/InventorySystem/blob/main/images/db.png)

### code to set uo your data base
```sql
CREATE DATABASE inventory;

USE inventory;

CREATE TABLE ict (
    id INT AUTO_INCREMENT PRIMARY KEY,
    serial VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    purchase_date DATE NOT NULL,
    location VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL,
    notes TEXT
);
```
