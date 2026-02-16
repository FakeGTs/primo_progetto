create table istituti (
  idistituto int primary key auto_increment,
  denominazione varchar(50) not null,
  indirizzo varchar(50) not null,
  telefono int(10) not null unique,
  provincia varchar(2) not null,
  citta varchar(50) not null
);

create table studenti(
  idstudente int primary key auto_increment,
  cognome varchar(50) not null,
  nome varchar(50) not null,
  datanascita date not null,
  classe varchar(2) not null, 
  idistituto int not null,
 CONSTRAINT fk_idistituto foreign key (idistituto) references istituti(idistituto)
);

create table manifestazioni (
  idmanifestazione int primary key auto_increment,
  descrizione varchar(100) not null,
  datainizio date not null,
  luogo varchar(50) not null
);

create table professori(
  idprofessore int primary key,
  cognome varchar(50) not null,
  nome varchar(50) not null,
  idmanifestazione int not null,
  idistituto int not null,
  foreign key (idmanifestazione) references manifestazioni(idmanifestazione),
  foreign key (idistituto) references istituti(idistituto)
);

create table partecipazioni(
  idstudente int ,
  idmanifestazione int,
  datainizio date not null,
  durata double not null,
  primary key( idstudente, idmanifestazione),
  foreign key (idstudente) references studenti(idstudente),
  foreign key (idmanifestazione) references manifestazioni(idmanifestazione)
);

insert into istituti (denominazione, indirizzo, telefono, provincia, citta) values
('itis rossi', 'via roma 10', '0123456789', 'VI', 'Vicenza'),
('liceo verdi', 'via milano 5', '0234567890', 'MI', 'Milano'),
('ipsia marconi', 'via torino 8', '0345678901', 'TO', 'Torino'),
('itc bianchi', 'via napoli 3', '0456789012', 'NA', 'Napoli');

insert into studenti (cognome, nome, datanascita, classe, idistituto) values
('Rossi', 'Luca', '2007-06-12', '4a', 1),
('Bianchi', 'Marco', '2006-09-21', '5b', 2),
('Verdi', 'Anna', '2007-01-30', '4c', 3),
('Neri', 'Giulia', '2006-11-18', '5a', 4);

insert into professori (idprofessore, cognome, nome, idmanifestazione, idistituto) values
(1, 'Ferrari', 'Paolo', 1, 1),
(2, 'Russo', 'Maria', 2, 2),
(3, 'Gallo', 'Luigi', 3, 3),
(4, 'Conti', 'Sara', 4, 4);

insert into manifestazioni (descrizione, datainizio, luogo) values
('torneo di calcio', '2026-03-10', 'Milano'),
('gara di atletica', '2026-04-05', 'Roma'),
('campionato basket', '2026-05-12', 'Torino'),
('corsa campestre', '2026-03-20', 'Firenze');

insert into partecipazioni (idstudente, idmanifestazione, datainizio, durata) values
(1, 1, '2026-03-10', 2.5),
(2, 2, '2026-04-05', 3.0),
(3, 3, '2026-05-12', 1.5),
(4, 4, '2026-03-20', 2.0);



