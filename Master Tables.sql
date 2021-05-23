
CREATE DATABASE IF NOT EXISTS  master_tables;
CREATE TABLE IF NOT EXISTS trainer_accounts
(
	trainer_id varchar(10) NOT NULL PRIMARY KEY,
	trainer_name varchar(30),
	email varchar(50) NOT NULL,
	password varchar(30) NOT NULL,
	created_date date NOT NULL,
	created_by varchar(30) NOT NULL,
	active boolean NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS trainer_details
(
	trainer_id varchar(10) NOT NULL PRIMARY KEY,
	trainer_name varchar(30) NOT NULL,
	trainer_email varchar(30) NOT NULL,
	trainer_phone_no varchar(15) NOT NULL,
	trainer_identity_proof varchar(50) NOT NULL,
	trainer_bank_account_no 	varchar(20) NOT NULL,
	trainer_ifsc_no	 varchar(20) ,	
	trainer_identity_number varchar(20) ,
	trainer_photo varchar(50) NOT NULL,
	approved boolean NOT NULL DEFAULT 0,
	approved_by	varchar(20) ,
	approved_date date
);
CREATE TABLE IF NOT EXISTS batch_details
(
	batch_id varchar(10) NOT NULL PRIMARY KEY,
	course_id varchar(10) NOT NULL ,
	level varchar(5) NOT NULL , 
	sessions int NOT NULL ,
	trainer_name varchar(30) NOT NULL ,
	batch_days varchar(50) NOT NULL, 
	start_time time NOT NULL,
	end_time time NOT NULL,
	student_names varchar(100),
	start_date date NOT NULL,
	stop_date date NOT NULL,
	next_date date NOT NULL ,
	FOREIGN KEY(level) REFERENCES levels_master(level)
);

CREATE TABLE IF NOT EXISTS trainer_address
(

	trainer_id varchar(10) NOT NULL PRIMARY KEY,
	address varchar(100) NOT NULL,
	address2 varchar(100),
	city varchar(30) NOT NULL, 
	state varchar(20),
	zip_code varchar(15),
	country varchar(30) NOT NULL
);


CREATE TABLE IF NOT EXISTS courses_master
( 
	course_id varchar(10) NOT NULL PRIMARY KEY,
	course_name	varchar(50) NOT NULL,
	age_group	varchar(10) ,
	active	boolean NOT NULL DEFAULT 0,
	course_desc	varchar(200),
	course_type	varchar(20)
);

CREATE TABLE IF NOT EXISTS levels_master
( 
	course_id varchar(10) NOT NULL PRIMARY KEY,
	level varchar(5) NOT NULL ,
	hours	int(2)  ,
	active	boolean NOT NULL DEFAULT 0

);
