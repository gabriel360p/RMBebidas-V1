-- drop database rmdrinks;
create database rmdrinks;

use rmdrinks;
 
 create table tb_usuarios(
 usu_codigo int primary key auto_increment not null ,
 usu_nome varchar(50),
 usu_sobrenome varchar(50),
 usu_email varchar(120),
 usu_senha varchar(120),
 usu_admin boolean
 );
 
create table tb_produtos(
 pro_codigo int primary key auto_increment not null,
 pro_nome varchar(45),
 pro_quantidade int,
 pro_descricao text,
 pro_fornecedor varchar(45),
 pro_preco double,
 pro_marca varchar(45)
 );
 
 insert into tb_usuarios (usu_nome,usu_sobrenome,usu_email,usu_senha,usu_admin) values ("admin","root","admin@admin","root",true); 