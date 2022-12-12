-- testing project tables

-- deleting any existing tables
delete from stock;
delete from sales;
delete from store_order;
delete from client_order;
delete from checkout;
delete from book;
delete from publisher;
delete from login;
delete from bank;

-- testing bank
INSERT INTO bank VALUES ('10001', 0);
INSERT INTO bank VALUES ('10002', 100.5);
--for publisher
INSERT INTO bank VALUES ('10003', 0);
INSERT INTO bank VALUES ('10004', 0);

--for login
INSERT INTO login
VALUES ('testClient', 'password', 'testClient@email.com', 'address', false, '10001');
INSERT INTO login
VALUES ('testAdmin', 'password', 'testAdmin@email.com', 'address', true, '10002');

--for publisher
INSERT INTO publisher
VALUES (DEFAULT, 'publisher', 'address', 'publisher@email.com', '000-000-000', '10003');

--for book
INSERT INTO book
VALUES ('123-4-56-789012-3', 'title', 'author', 'genre', 5, DEFAULT, 5, 5.00, 0);

--for stock
INSERT INTO stock
VALUES ('123-4-56-789012-3', 5);

--for checkout
INSERT INTO checkout
VALUES (DEFAULT, 'testClient', '123-4-56-789012-3', 'title', 10, 5);

--for client_order
INSERT INTO client_order
VALUES (DEFAULT, 'testClient', 'ship_address', 'bill_address', 'In Transit', DEFAULT, 20);

--for store_order
INSERT INTO store_order
VALUES (DEFAULT, '123-4-56-789012-3', 5, 'In Transit');

--for sales
INSERT INTO sales
VALUES (DEFAULT, 50);