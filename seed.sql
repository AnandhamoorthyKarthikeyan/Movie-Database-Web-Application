INSERT INTO Movies (title, release_year, genre, rating) VALUES
('The Shawshank Redemption', 1994, 'Drama', 9.3),
('The Godfather', 1972, 'Crime', 9.2),
('The Dark Knight', 2008, 'Action', 9.0),
('Inception', 2010, 'Sci-Fi', 8.8),
('Interstellar', 2014, 'Sci-Fi', 8.6),
('Parasite', 2019, 'Thriller', 8.6),
('Whiplash', 2014, 'Drama', 8.5),
('Spirited Away', 2001, 'Animation', 8.6),
('Mad Max: Fury Road', 2015, 'Action', 8.1),
('The Social Network', 2010, 'Drama', 7.8);

INSERT INTO Actors (name) VALUES
('Tim Robbins'),
('Morgan Freeman'),
('Marlon Brando'),
('Al Pacino'),
('Christian Bale'),
('Heath Ledger'),
('Leonardo DiCaprio'),
('Elliot Page'),
('Matthew McConaughey'),
('Anne Hathaway'),
('Song Kang-ho'),
('J.K. Simmons'),
('Miles Teller'),
('Rumi Hiiragi'),
('Charlize Theron'),
('Jesse Eisenberg'),
('Andrew Garfield');

-- Links (minimal, just to show joins)
-- Shawshank
INSERT INTO Movie_Actors VALUES (1,1);
INSERT INTO Movie_Actors VALUES (1,2);

-- Godfather
INSERT INTO Movie_Actors VALUES (2,3);
INSERT INTO Movie_Actors VALUES (2,4);

-- Dark Knight
INSERT INTO Movie_Actors VALUES (3,5);
INSERT INTO Movie_Actors VALUES (3,6);

-- Inception
INSERT INTO Movie_Actors VALUES (4,7);
INSERT INTO Movie_Actors VALUES (4,8);

-- Interstellar
INSERT INTO Movie_Actors VALUES (5,9);
INSERT INTO Movie_Actors VALUES (5,10);

-- Parasite
INSERT INTO Movie_Actors VALUES (6,11);

-- Whiplash
INSERT INTO Movie_Actors VALUES (7,12);
INSERT INTO Movie_Actors VALUES (7,13);

-- Spirited Away
INSERT INTO Movie_Actors VALUES (8,14);

-- Mad Max: Fury Road
INSERT INTO Movie_Actors VALUES (9,15);

-- The Social Network
INSERT INTO Movie_Actors VALUES (10,16);
INSERT INTO Movie_Actors VALUES (10,17);
