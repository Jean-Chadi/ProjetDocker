CREATE TABLE Livre (
 id INT UNSIGNED NOT NULL AUTO_INCREMENT,
 titre VARCHAR(200),
 prix FLOAT(6, 2),
 genre VARCHAR(60),
 PRIMARY KEY(id)
)
ENGINE=INNODB;