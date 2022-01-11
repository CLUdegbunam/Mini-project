CREATE TABLE products (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL,
    price float NOT NULL
 );

 CREATE TABLE couriers (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL,
    phone INT(50) NOT NULL
 );

 CREATE TABLE orders (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customer_name varchar(255) NOT NULL,
    customer_address VARCHAR(255) NOT NULL,
    customer_phone INT NOT NULL,
    courier_id INT NOT NULL,
    status_id int NOT NULL,
    items VARCHAR(255) NOT NULL,
    foreign key (courier_id) references couriers(id),
    foreign key (status_id) references status(status_id)
 );

