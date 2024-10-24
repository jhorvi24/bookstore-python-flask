/*
	Database Creation Script for the web page
*/
DROP DATABASE IF EXISTS bookstore_db;

CREATE DATABASE bookstore_db;

USE bookstore_db;

/* Create Books table. */

CREATE TABLE Books(
  ISBN INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200) NOT NULL DEFAULT '',
  author TEXT NOT NULL DEFAULT '',
  description VARCHAR(200) NOT NULL DEFAULT '',
  image_url VARCHAR(256) DEFAULT 'static/images/default-image.jpg',
  amount INT NOT NULL,
  price FLOAT NOT NULL
  );

/* INSERT initialization data into the Books table. */

INSERT INTO Books (title, author, description, image_url, amount, price) VALUES
	  ('El principito', 'Antoine de Saint-Exupery', 'Libro infantil que fomenta la creatividad', 'static/images/principito.jpg',15, 20)
	, ('Cien años de soledad', 'Gabriel Garcia Marquez', 'Novela de literatura', 'static/images/ciensoledad.png', 23,43.5)
	, ('El diario de Ana Frank', 'Ana Frank', 'Libro sobre la ocupación Nazi en Holanda', 'static/images/ana.png',12,15)
	, ('El retrato de Dorian Gray', 'Oscar Wilde', 'Libro de ficción','static/images/retrato.jpg',5,13.2);

/* Create Users table */
CREATE TABLE Users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  email VARCHAR(100) NOT NULL,
  budget DECIMAL(10, 2) DEFAULT 100.00
);

/* Insert some sample data into the Users table */
INSERT INTO Users (username, password_hash, email, budget) VALUES
  ('user1', 'password1', 'user1@example.com', 100.00),
  ('user2', 'password2', 'user2@example.com', 150.50),
  ('user3', 'password3', 'user3@example.com', 75.25);
