CREATE TABLE premia (
    id varchar(20) PRIMARY KEY,
    premia NUMERIC
);

CREATE TABLE dzial (
    id INTEGER PRIMARY KEY,
    nazwa VARCHAR(20),
    siedziba dzialu VARCHAR(20)
);

CREATE TABLE pracownicy (
    id VARCHAR PRIMARY KEY, 
    nazwisko VARCHAR(20),
    imie VARCHAR(20),
    stanowisko VARCHAR(20),
    data_zatr VARCHAR(23),
    placa NUMERIC,
    id_dzial INTEGER,
    premia NUMERIC DEFAULT 0,
    FOREIGN KEY(stanowisko) REFERENCES premia(id),
    FOREIGN KEY(id_dzial) REFERENCES dzial(id)
);
