-- create a simple table users 
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) UNIQUE NOT NULL,
	name varchar(255)
);
