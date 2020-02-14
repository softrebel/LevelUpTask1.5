DROP DATABASE IF EXISTS levelup;

CREATE DATABASE levelup
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;


--
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE levelup;

--
-- Create table `customer`
--
CREATE TABLE customer (
  ID int(11) NOT NULL AUTO_INCREMENT,
  name varchar(50) DEFAULT NULL,
  is_enable tinyint(4) DEFAULT 1,
  created_by varchar(255) DEFAULT NULL,
  created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  update_by varchar(255) DEFAULT NULL,
  updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (ID)
)
ENGINE = INNODB,
AUTO_INCREMENT = 86,
AVG_ROW_LENGTH = 546,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Create table `product`
--
CREATE TABLE product (
  ID int(11) NOT NULL AUTO_INCREMENT,
  name varchar(50) DEFAULT NULL,
  customerId int(11) NOT NULL,
  is_enable tinyint(4) NOT NULL DEFAULT 1,
  PRIMARY KEY (ID)
)
ENGINE = INNODB,
AUTO_INCREMENT = 3091,
AVG_ROW_LENGTH = 54,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Create foreign key
--
ALTER TABLE product
ADD CONSTRAINT FK_product_customerId FOREIGN KEY (customerId)
REFERENCES customer (ID) ON DELETE NO ACTION;

--
-- Create table `source`
--
CREATE TABLE source (
  ID int(11) NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  is_premium tinyint(4) NOT NULL DEFAULT 0,
  is_enable tinyint(4) NOT NULL DEFAULT 1,
  PRIMARY KEY (ID)
)
ENGINE = INNODB,
AUTO_INCREMENT = 17,
AVG_ROW_LENGTH = 3276,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Create table `offer`
--
CREATE TABLE offer (
  ID int(11) NOT NULL AUTO_INCREMENT,
  userId int(11) DEFAULT NULL,
  productId int(11) NOT NULL,
  sourceId int(11) DEFAULT NULL,
  `order` int(11) DEFAULT 0,
  created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (ID)
)
ENGINE = INNODB,
AUTO_INCREMENT = 21895,
AVG_ROW_LENGTH = 72,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;

--
-- Create foreign key
--
ALTER TABLE offer
ADD CONSTRAINT FK_offer_productId FOREIGN KEY (productId)
REFERENCES product (ID) ON DELETE NO ACTION;

--
-- Create foreign key
--
ALTER TABLE offer
ADD CONSTRAINT FK_offer_sourceId FOREIGN KEY (sourceId)
REFERENCES source (ID) ON DELETE NO ACTION;
