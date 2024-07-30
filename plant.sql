
DROP TABLE IF EXISTS plant;
DROP TABLE IF EXISTS zombies;
DROP TABLE IF EXISTS login_info;


CREATE TABLE IF NOT EXISTS login_info(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE IF NOT EXISTS plant(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    health INTEGER,
    hits INTEGER,
    login_info_id INTEGER,
    FOREIGN KEY(login_info_id) REFERENCES login_info(id)
);

CREATE TABLE IF NOT EXISTS zombies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    health INTEGER,
    hits INTEGER,
    plant_id INTEGER,
    FOREIGN KEY(plant_id) REFERENCES plant(id)
);



INSERT INTO login_info(name)
VALUES("Gray");

INSERT INTO plant(name, health, hits, login_info_id)
VALUES("PeaShooter", 999999, 555555, 0);
INSERT INTO plant(name, health, hits)
VALUES("SunFlower", 999988, 77773);
INSERT INTO plant(name, health, hits)
VALUES("Chomper", 1000000000, 23);

INSERT INTO zombies(name,health, hits)
VALUES("Normal Zombie", 500, 125);
INSERT INTO zombies(name,health, hits)
VALUES("Bucket Zombie", 700, 233);