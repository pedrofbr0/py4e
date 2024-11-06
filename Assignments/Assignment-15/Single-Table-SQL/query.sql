CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
DELETE FROM Ages;

INSERT INTO Ages (name, age) VALUES ('Ryese', 30);
INSERT INTO Ages (name, age) VALUES ('Nabiha', 37);
INSERT INTO Ages (name, age) VALUES ('Hussnain', 24);
INSERT INTO Ages (name, age) VALUES ('Megha', 23);

SELECT hex(name || age) AS X FROM Ages ORDER BY X