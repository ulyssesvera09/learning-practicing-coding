CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, pub_house TEXT, price INTEGER);

INSERT INTO books VALUES(1, "Pasado anterior", "Salvador Elizondo", "FCE", 100);
INSERT INTO books VALUES(2, "Tercer libro de Pantagruel", "Francois Rabelais", "Catedra", 250);
INSERT INTO books VALUES(3, "El libro de las ilusiones", "Paul Auster", "booket", 100);
INSERT INTO books VALUES(4, "Balun Canan", "Rosario Castellanos", "FCE", 100);
INSERT INTO books VALUES(5, "La palabra y el punyo", "Gerardo Ramirez", "IIFl", 50);
INSERT INTO books VALUES(6, "El va y ven de las Malvinas", "Fernando del Paso", "FCE", 80);
INSERT INTO books VALUES(7, "Legenda aurea", "Jacobus de Voragine", "Philipp Reclam", 150);
INSERT INTO books VALUES(8, "Prinzipien christlicher Moral", "Joseph Ratzinger", "Johannes", 200);
INSERT INTO books VALUES(9, "Philosophen der Antike II", "Friedo Ricken", "Kohlhammer", 300);
INSERT INTO books VALUES(10, "Les confessions: I-VII", "Saint Augustin", "Etudes augustiniennes", 200);
INSERT INTO books VALUES(11, "Les confessions: VIII-XIII", "Saint Augustin", "Etudes augustiniennes", 200);
INSERT INTO books VALUES(12, "Les commentaires des psaumes", "Saint Augustin", "Etudes augustiniennes", 250);
INSERT INTO books VALUES(13, "Istmicas", "Pindaro", "Bibliotheca Mexicana Scriptorum", 100);
INSERT INTO books VALUES(14, "Suenyo de Escipion", "Ciceron", "Bibliotheca Mexicana Scriptorum", 150);
INSERT INTO books VALUES(15, "De suo reditu", "Rutilio Namaciano", "Gredos", 200);

SELECT SUM(price) from books;
SELECT pub_house from books;
