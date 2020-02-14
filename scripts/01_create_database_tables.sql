DROP DATABASE IF EXISTS levelup;

CREATE DATABASE levelup
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;


USE levelup;

--
-- Create table `Customer`
--
CREATE TABLE customer (
  ID INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) DEFAULT NULL,
  is_enable TINYINT(4) DEFAULT 1,
  created_by VARCHAR(255) DEFAULT NULL,
  created_at DATETIME NOT NULL DEFAULT NOW(),
  update_by VARCHAR(255) DEFAULT NULL,
  updated_at DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (ID)
)
ENGINE = INNODB;

--
-- Create table `product`
--
CREATE TABLE product (
  ID INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) DEFAULT NULL,
  is_enable TINYINT(4) NOT NULL DEFAULT 1,
  PRIMARY KEY (ID)
)

ENGINE = INNODB;


--
-- Create table `source`
--
CREATE TABLE source (
  ID INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  is_enable TINYINT(4) NOT NULL DEFAULT 1,
  PRIMARY KEY (ID)
)
ENGINE = INNODB;
--
-- Create table `offer`
--
CREATE TABLE offer (
  ID INT(11) NOT NULL AUTO_INCREMENT,
  userId INT(11) NOT NULL,
  productId INT(11) NOT NULL,
  sourceId INT(11) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (ID)
)
ENGINE = INNODB;

--
-- Create foreign key
--
ALTER TABLE offer 
  ADD CONSTRAINT FK_offer_productId FOREIGN KEY (productId)
    REFERENCES product(ID) ON DELETE NO ACTION;

--
-- Create foreign key
--
ALTER TABLE offer 
  ADD CONSTRAINT FK_offer_sourceId FOREIGN KEY (sourceId)
    REFERENCES source(ID) ON DELETE NO ACTION;



USE levelup;
INSERT INTO source(ID, name, is_enable) VALUES(1, 'free', 1);
INSERT INTO source(ID, name, is_enable) VALUES(2, 'premium', 1);
