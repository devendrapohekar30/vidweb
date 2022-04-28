create database vidweb;

use vidweb;




CREATE TABLE user(
  user_id int NOT NULL,
  user_name varchar(100) NOT NULL,
  contact varchar(100) NOT NULL,
  username varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  password varchar(100) NOT NULL,
  constraint user_pk primary key(user_id)
);

insert into user(user_name,contact) values
	('Devendra',9109396802),
    ('Rideshnath',6264736064),
    ('Yogesh',3435675872),
    ('Ganpat',3345468883),
    ('Harshal',7218023412);



/*create table lose(
vege_name varchar(50),
vege_price varchar(50) not null,
vege_quantity int not null,
fruit_name varchar(50),
fruit_price varchar(50) not null,
fruit_quantity int not null
);*/

create table bolywood(
bolywood_id int not null auto_increment,
song_name varchar(100000),
constraint bolywood_pk primary key(bolywood_id)
);


insert into bolywood(song_name) values
	('Tum hi ho'),
    ('Agar tum sath ho'),
    ('Raata Lambiya'),
    ('Teri mitti me '),
    ('The breakup song'),
    ('Kutti song');


create table gallary(
gallay_id int not null auto_increment,
gallary_name varchar(50),

constraint gallary_pk primary key(gallary_id)
);

insert into gallary(gallary_name,) values
	('Apple','50kg',30),
    ('Banana','40kg',20),
    ('Grapes','20kg',30),
    ('Cherry','70kg',40),
    ('Orange','10kg',60),
    ('Chickoo','25kg',50);
    


create table cart(
cart_id int not null,
vege_name varchar(50),
vegeqty_taken int not null,
fruit_name varchar(50),
fruitqty_taken int not null,
vproduct_id int,
fproduct_id int,
constraint cart_pk primary key(cart_id),
foreign key(vproduct_id) references vege(vproduct_id),
foreign key(fproduct_id) references fruit(fproduct_id)
);



create table purchase(
product_id int not null,
products varchar(200),
total_amount int not null,
constraint product_pk primary key(product_id)
);


  
    
alter table customer
	modify customer_id int not null auto_increment;
    



alter table cart
	modify cart_id int not null auto_increment,auto_increment=1000;
    
alter table purchase
	modify product_id int not null auto_increment;
    
    
    









