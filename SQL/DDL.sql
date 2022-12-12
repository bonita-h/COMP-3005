CREATE TABLE IF NOT EXISTS bank (
	bankAccountID	varchar(20),
	balance			numeric(9, 2),
	primary key(bankAccountID)
);

CREATE TABLE IF NOT EXISTS login (
	username		varchar(20),
	password 		varchar(20),
	email			varchar(20),
	address			varchar(20),
	admin			boolean,
	bankAccountID	varchar(20),
	--determines whether they are a customer or owner
	primary key(username),
	foreign key(bankAccountID) 
		references bank(bankAccountID)
);

CREATE TABLE IF NOT EXISTS publisher (
	pID				serial,
	pname 			varchar(20),
	address			varchar(20),
	email			varchar(20),
	phoneNumber		varchar(20),
	bankAccountID	varchar(20),
	primary key(pID),
	foreign key(bankAccountID) 
		references bank(bankAccountID)
);

CREATE TABLE IF NOT EXISTS book (
	--searching for book
	ISBN		varchar(20),
	title		varchar(20),
	author		varchar(20),
	genre		varchar(20),
	--other info
	quantity	int check(quantity > -1),
	publisher	serial,
	pages		int,
	price		numeric(5, 2),
	expidenture numeric(5, 2), --for publisher sales
	primary key(ISBN),
	foreign key (publisher)
		references publisher(pID)
);

CREATE TABLE IF NOT EXISTS stock (
	ISBN	varchar(20),
	quantity int check(quantity > -1),
	primary key(ISBN), 
	foreign key(ISBN)
		references book(ISBN)
);

CREATE TABLE IF NOT EXISTS checkout (
	--checkout for user
	orderID		serial,
	username	varchar(20),
	--book info
	ISBN		varchar(20),
	title		varchar(20),
	price		numeric(5, 2),
	quantity	int,
	primary key(orderID),
	foreign key(username) 
		references login(username),
	foreign key(ISBN)
		references book(ISBN)
);

CREATE TABLE IF NOT EXISTS client_order (
	orderID			serial,
	-- delivery info
	username		varchar(20),
	ship_address	varchar(20),
	bill_address	varchar(20),
	progress		varchar(20)
		check (progress in ('Not Shipped', 'In Transit', 'Delivered')),
	-- book info
	ISBN			varchar(20),
	price			numeric(5, 2),
	primary key(orderID),
	foreign key(orderID)
		references checkout(orderID),
	foreign key(username)
		references login(username),
	foreign key (ISBN)
		references book(ISBN)
);

CREATE TABLE IF NOT EXISTS store_order (
	orderID			serial,
	ISBN			varchar(20),
	quantity		int,
	progress		varchar(20)
		check (progress in ('Not Shipped', 'In Transit', 'Delivered')),
	primary key(orderID),
	foreign key(ISBN) 
		references book(ISBN)
	
);

CREATE TABLE IF NOT EXISTS sales (
	orderID	serial,
	total	numeric(5, 2),
	primary key(orderID),
	foreign key (orderID)
		references checkout(orderID)
);

