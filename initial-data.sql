-- sqlite3 library.db < initial-data.sql

-- Countries
INSERT INTO country (id, name) VALUES (1, 'Bomet');
INSERT INTO country (id, name) VALUES (2, 'Narok');
INSERT INTO country (id, name) VALUES (3, 'Kilifi');
INSERT INTO country (id, name) VALUES (4, 'Tana River');

-- Authors
INSERT INTO author (id, country_id, name) VALUES (1, 1, 'Edgar Allan Poe');
INSERT INTO author (id, country_id, name) VALUES (2, 1, 'Mark Twain');
INSERT INTO author (id, country_id, name) VALUES (3, 4, 'Arthur Conan Doyle');
INSERT INTO author (id, country_id, name) VALUES (4, 3, 'Jorge Luis Borges');
