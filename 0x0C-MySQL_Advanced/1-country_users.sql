-- create a simple table users
-- Add Country us, co, tn 
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) UNIQUE NOT NULL,
	name varchar(255),
	country ENUM( 'US', 'CO' , 'TN' ) NOT NULL
);
