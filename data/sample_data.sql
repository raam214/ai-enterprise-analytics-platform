CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    region VARCHAR(50),
    signup_date DATE,
    is_active BOOLEAN
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price NUMERIC
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    transaction_date DATE,
    amount NUMERIC
);

INSERT INTO customers VALUES
(1,'Amit Sharma','amit@gmail.com','North','2024-01-10',true),
(2,'Priya Verma','priya@gmail.com','West','2024-02-15',true),
(3,'Rahul Mehta','rahul@gmail.com','South','2023-11-05',false),
(4,'Neha Singh','neha@gmail.com','East','2024-03-01',true),
(5,'Karan Patel','karan@gmail.com','West','2023-12-20',true);

INSERT INTO products VALUES
(1,'Laptop',65000),
(2,'Phone',30000),
(3,'Headphones',2500),
(4,'Monitor',12000),
(5,'Keyboard',1800);

INSERT INTO transactions VALUES
(1,1,1,'2024-04-01',65000),
(2,2,2,'2024-04-03',30000),
(3,3,3,'2024-03-15',2500),
(4,4,4,'2024-04-05',12000),
(5,5,5,'2024-04-06',1800),
(6,1,2,'2024-04-10',30000);
