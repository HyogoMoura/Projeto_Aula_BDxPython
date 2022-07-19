create database SmartList
default character  set utf8
default collate utf8_general_ci;

create table Users (
U_id int not null auto_increment,
name varchar(40),
cpf varchar(15),
phone varchar(20),
mail varchar (50),
location varchar(60),
primary key (U_id)
)default charset = utf8;

create table Store (
S_id int not null auto_increment,
name varchar(30),
location varchar(60),
comutecost varchar(10),
primary key (S_id)
) default charset = utf8;

create table Product (
P_id int not null auto_increment,
description varchar (60),
label varchar(30),
getin varchar(30),
unitvaluer float,
unit varchar (20),
amount float,
primary key (P_id)
) default charset = utf8;

create table Cart_Plist (
Cp_id int not null,
primary key (Cp_id)
) default charset = utf8;

create table Evaluation (
Ev_id int not null auto_increment,
description text,
rate varchar(5),
primary key (Ev_id)
) default charset = utf8;


create table Cart (
Ca_id int not null auto_increment,
Cartdate varchar(30),
totalvaluer float,
totalamount int,
primary key (Ca_id)
)default charset = utf8;


/*Adicionando colunas e linkando chaves estrangeiras para tabela lista de produtos
*/

alter table Cart_Plist
add column ProductID int,
add column CartID int;
alter table Cart_Plist
add foreign key (ProductID)
references product (P_id);
alter table Cart_Plist
add foreign key (CartID)
references cart (Ca_id);

/*Adicionando colunas e linkando chaves estrangeiras para tabela  carrinho
*/
alter table Cart
add column UserID int,
add column StoreID int,
add column ListID int,
add column RateID int;
alter table Cart
add foreign key (UserID)
references Users (U_id);
alter table Cart
add foreign key (StoreID)
references store (S_id);
alter table Cart
add foreign key (ListID)
references cart_plist (Cp_id);
alter table Cart
add foreign key (RateID)
references evaluation (Ev_id);

