CREATE DATABASE LittleLemon;

USE LittleLemon;

CREATE TABLE Customers (
    CustomerID VARCHAR(20) PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    CountryCode VARCHAR(10),
    Region VARCHAR(100)
);

CREATE TABLE Orders (
    OrderID VARCHAR(20) PRIMARY KEY,
    OrderDate DATE,
    DeliveryDate DATE,
    CustomerID VARCHAR(20),
    Sales FLOAT,
    Quantity INT,
    Discount FLOAT,
    DeliveryCost FLOAT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems (
    OrderID VARCHAR(20),
    CourseName VARCHAR(100),
    CuisineName VARCHAR(100),
    StarterName VARCHAR(100),
    DesertName VARCHAR(100),
    Drink VARCHAR(100),
    Sides VARCHAR(100),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
