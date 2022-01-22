drop table if EXISTS users;

create table users(api_key varchar(100) not null primary key UNIQUE, username varchar(50) not NULL, email varchar(50) not null UNIQUE, password varchar(50) not null);