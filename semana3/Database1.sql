CREATE TABLE IF NOT EXISTS area (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL	
);
--insert
INSERT INTO area(name) VALUES('ventas');
INSERT INTO area VALUES (6,'prueba');
INSERT INTO area (name) VALUES ('Marketing'),('RxH');
INSERT INTO customer (name,area_id) VALUES
('Jose Arriola',1),('ROberto Quiroga',2),('Joseph Flores',3),('Jessica Chiu',4),('Germania toro',NULL);

--update - 	MO OLVIDAR EL WHERE !!
UPDATE area SET name='Recursos Humanos'	WHERE id=4;

--DELETE - NO OLVIDAR EL WHERE !!
DELETE FROM area WHERE id=6;

--JOINS
--INNER JOIN ->INTERSECCION
SELECT --*
	C.id as customer_id,
	c.name as customer_name,
	a.name as area_name
	
FROM area a 
INNER JOIN customer c
ON a.id=c.area_id;

