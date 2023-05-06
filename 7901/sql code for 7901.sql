DROP TABLE IF EXISTS cabin;
DROP TABLE IF EXISTS disable_cabin;
DROP TABLE IF EXISTS smoking_cabin;
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS cruise;
DROP TABLE IF EXISTS manifest;
DROP TABLE IF EXISTS operator;
DROP TABLE IF EXISTS passenger;
DROP TABLE IF EXISTS ship;

CREATE TABLE cabin (
    ship_code      INT(4) NOT NULL,
    cabin_no       INT(5) NOT NULL,
    cabin_capacity INT(1) NOT NULL,
    cabin_class    ENUM('B', 'I', 'O', 'S') NOT NULL,
    PRIMARY KEY (cabin_no, ship_code)
);

ALTER TABLE cabin MODIFY COLUMN ship_code INT(4) NOT NULL COMMENT 'Identifier for ship';
ALTER TABLE cabin MODIFY COLUMN cabin_no INT(5) NOT NULL COMMENT 'Cabin number on given ship';
ALTER TABLE cabin MODIFY COLUMN cabin_capacity INT(1) NOT NULL COMMENT 'Sleeping capacity for cabin';
ALTER TABLE cabin MODIFY COLUMN cabin_class ENUM('B', 'I', 'O', 'S') NOT NULL COMMENT 'WC class of the cabin (B Balcony, I Interior, O Ocean View, S Suite)';


CREATE TABLE country (
    country_code CHAR(2) NOT NULL,
    country_name VARCHAR(40) NOT NULL,
    PRIMARY KEY (country_code)
) COMMENT='Country information';

ALTER TABLE country MODIFY COLUMN country_code CHAR(2) COMMENT 'Country code';
ALTER TABLE country MODIFY COLUMN country_name VARCHAR(40) COMMENT 'Country name';



CREATE TABLE cruise (
    cruise_id                 INT(6) NOT NULL,
    cruise_name               VARCHAR(80) NOT NULL,
    cruise_description        VARCHAR(200) NOT NULL,
    ship_code                 INT(4) NOT NULL,
    cruise_departure_datetime DATETIME NOT NULL,
    cruise_duration           INT(2) NOT NULL,
    PRIMARY KEY (cruise_id)
);

ALTER TABLE cruise MODIFY COLUMN cruise_id INT(6) NOT NULL COMMENT 'Cruise identifier - used only for a single cruise';
ALTER TABLE cruise MODIFY COLUMN cruise_name VARCHAR(80) NOT NULL COMMENT 'Name of cruise';
ALTER TABLE cruise MODIFY COLUMN cruise_description VARCHAR(200) NOT NULL COMMENT 'Description of cruise';
ALTER TABLE cruise MODIFY COLUMN ship_code INT(4) NOT NULL COMMENT 'Identifier for ship';
ALTER TABLE cruise MODIFY COLUMN cruise_departure_datetime DATETIME NOT NULL COMMENT 'Cruise scheduled departure datetime';
ALTER TABLE cruise MODIFY COLUMN cruise_duration INT(2) NOT NULL COMMENT 'Cruise duration in days';


CREATE TABLE ship (
    ship_code           INT(4) NOT NULL,
    ship_name           VARCHAR(20) NOT NULL,
    ship_guest_capacity INT(4) NOT NULL,
    country_code        CHAR(2) NOT NULL,
    PRIMARY KEY (ship_code)
);

ALTER TABLE ship MODIFY COLUMN ship_code INT(4) NOT NULL COMMENT 'Identifier for ship';
ALTER TABLE ship MODIFY COLUMN ship_name VARCHAR(20) NOT NULL COMMENT 'Name of ship';
ALTER TABLE ship MODIFY COLUMN ship_guest_capacity INT(5) NOT NULL COMMENT 'Ships passenger capacity';
ALTER TABLE ship MODIFY COLUMN country_code CHAR(2) NOT NULL COMMENT 'Country code';


CREATE TABLE passenger (
    passenger_id      INT(6) NOT NULL,
    passenger_fname   VARCHAR(30),
    passenger_lname   VARCHAR(30),
    passenger_dob     DATE NOT NULL,
    passenger_gender  ENUM('M', 'F', 'X') NOT NULL,
    passenger_contact CHAR(10),
    PRIMARY KEY (passenger_id),
    CONSTRAINT passenger_un UNIQUE (passenger_contact)
) COMMENT='Table containing information about passengers.';

ALTER TABLE passenger MODIFY COLUMN passenger_id INT(6) NOT NULL COMMENT 'Unique identifier for a passenger';

ALTER TABLE passenger MODIFY COLUMN passenger_fname VARCHAR(30) COMMENT 'Passenger first name';

ALTER TABLE passenger MODIFY COLUMN passenger_lname VARCHAR(30) COMMENT 'Passenger last name';

ALTER TABLE passenger MODIFY COLUMN passenger_dob DATE NOT NULL COMMENT 'Passenger`s date of birth';

ALTER TABLE passenger MODIFY COLUMN passenger_gender ENUM('M', 'F', 'X') NOT NULL COMMENT 'Passenger gender(M for male, F for female, or X for non-binary/indeterminate/intersex/unspecified/other)';

ALTER TABLE passenger MODIFY COLUMN passenger_contact CHAR(10) COMMENT 'Passenger contact phone number';


CREATE TABLE disable_cabin (
    ship_code      INT(4) NOT NULL,
    cabin_no       INT(5) NOT NULL,
    auxiliary_facilities    ENUM('Y', 'N', 'U') NOT NULL,
    PRIMARY KEY (cabin_no, ship_code)
);

ALTER TABLE disable_cabin MODIFY COLUMN ship_code INT(4) NOT NULL COMMENT 'Identifier for ship';
ALTER TABLE disable_cabin MODIFY COLUMN cabin_no INT(5) NOT NULL COMMENT 'Cabin number on given ship';
ALTER TABLE disable_cabin MODIFY COLUMN auxiliary_facilitiess ENUM('Y', 'N', 'U') NOT NULL COMMENT 'Y for yes, N for no, U for Unknown';


CREATE TABLE smoking_cabin (
    ship_code      INT(4) NOT NULL,
    cabin_no       INT(5) NOT NULL,
    ashtrays     ENUM('Y', 'N', 'U') NOT NULL,
    PRIMARY KEY (cabin_no, ship_code)
);

ALTER TABLE smoking_cabin MODIFY COLUMN ship_code INT(4) NOT NULL COMMENT 'Identifier for ship';
ALTER TABLE smoking_cabin MODIFY COLUMN cabin_no INT(5) NOT NULL COMMENT 'Cabin number on given ship';
ALTER TABLE smoking_cabin MODIFY COLUMN ashtrays  ENUM('Y', 'N', 'U') NOT NULL COMMENT 'Y for yes, N for no, U for Unknown';

ALTER TABLE ship
    ADD CONSTRAINT country_ship FOREIGN KEY ( country_code )
        REFERENCES country ( country_code );

ALTER TABLE disable_cabin
    ADD CONSTRAINT cabin_disable_cabin_ship FOREIGN KEY ( ship_code )
        REFERENCES ship ( ship_code ),
    ADD CONSTRAINT cabin_disable_cabin_cabin FOREIGN KEY ( cabin_no )
        REFERENCES cabin ( cabin_no );

ALTER TABLE smoking_cabin
    ADD CONSTRAINT smoking_cabin_ship FOREIGN KEY ( ship_code )
        REFERENCES ship ( ship_code ),
    ADD CONSTRAINT smoking_cabin_cabin FOREIGN KEY ( cabin_no )
        REFERENCES cabin ( cabin_no );

ALTER TABLE cruise
    ADD CONSTRAINT ship_cruise FOREIGN KEY ( ship_code )
        REFERENCES ship ( ship_code );


CREATE TABLE manifest (
    manifest_id             INT(7) NOT NULL,
    passenger_id            INT(6) NOT NULL,
    cruise_id               INT(6) NOT NULL,
    manifest_board_datetime DATE,
    ship_code               INT(4) NOT NULL,
    cabin_no                INT(5) NOT NULL,
    PRIMARY KEY (manifest_id),
    UNIQUE (passenger_id, cruise_id)
);
ALTER TABLE manifest MODIFY COLUMN manifest_id INT(7) NOT NULL COMMENT 'Unique identifier for a manifest';
ALTER TABLE manifest MODIFY COLUMN passenger_id INT(6) NOT NULL COMMENT 'Unique identifier for a passenger';
ALTER TABLE manifest MODIFY COLUMN cruise_id INT(6) NOT NULL COMMENT 'Cruise identifier - used only for a single cruise';
ALTER TABLE manifest MODIFY COLUMN manifest_board_datetime DATE COMMENT 'Date/time passenger boarded ship';
ALTER TABLE manifest MODIFY COLUMN ship_code INT(4) NOT NULL COMMENT 'Identifier for ship';
ALTER TABLE manifest MODIFY COLUMN cabin_no INT(5) NOT NULL COMMENT 'Cabin number on given ship';

CREATE INDEX cabin_ship_cabin_no_idx ON cabin (ship_code, cabin_no);

ALTER TABLE manifest
    ADD CONSTRAINT cabin_manifest FOREIGN KEY ( ship_code, cabin_no )
        REFERENCES cabin ( ship_code, cabin_no );

ALTER TABLE manifest
    ADD CONSTRAINT passenger_manifest FOREIGN KEY ( passenger_id )
        REFERENCES passenger ( passenger_id );

ALTER TABLE manifest
    ADD CONSTRAINT cruise_manifest FOREIGN KEY ( cruise_id )
        REFERENCES cruise ( cruise_id );



INSERT INTO country(country_code, country_name)
VALUES('CN', 'China');
INSERT INTO country(country_code, country_name)
VALUES('AM', 'Armenia');
INSERT INTO country(country_code, country_name)
VALUES('AU', 'Australia');
INSERT INTO country(country_code, country_name)
VALUES('BR', 'Brazil');
INSERT INTO country(country_code, country_name)
VALUES('CA', 'Canada');
INSERT INTO country(country_code, country_name)
VALUES('FO', 'Faroe Islands');
INSERT INTO country(country_code, country_name)
VALUES('FJ', 'Fiji');
INSERT INTO country(country_code, country_name)
VALUES('FI', 'Finland');
INSERT INTO country(country_code, country_name)
VALUES('FR', 'France');


INSERT INTO ship(
    ship_code,
    ship_name,
    ship_guest_capacity,
    country_code
)
VALUES(110, 'Beijing', 5000, 'CN');
INSERT INTO ship(
    ship_code,
    ship_name,
    ship_guest_capacity,
    country_code
)
VALUES(
    102,
    'Carnival Splendor',
    1864,
    'AM'
);
INSERT INTO ship(
    ship_code,
    ship_name,
    ship_guest_capacity,
    country_code
)
VALUES(
    103,
    'Majestic Princess',
    2240,
    'AU'
);
INSERT INTO ship(
    ship_code,
    ship_name,
    ship_guest_capacity,
    country_code
)
VALUES(104, 'Queen Mary 2', 4328, 'BR');
INSERT INTO ship(
    ship_code,
    ship_name,
    ship_guest_capacity,
    country_code
)
VALUES(105, 'Luminos', 1240, 'CA');
INSERT INTO ship(
    ship_code,
    ship_name,
    ship_guest_capacity,
    country_code
)
VALUES(106, 'Coral Princess', 1860, 'FO');
INSERT INTO ship(
    ship_code,
    ship_name,
    ship_guest_capacity,
    country_code
)


INSERT INTO cruise(
    cruise_id,
    cruise_name,
    cruise_description,
    ship_code,
    cruise_departure_datetime,
    cruise_duration
)
VALUES(
    2,
    'Melbourne to Sydney',
    '2 nights at sea from Melbourne to Sydney.',
    102,
    STR_TO_DATE(
        '16-Apr-2022 9:00',
        '%d-%b-%Y %H:%i'
    ),
    2
);

INSERT INTO cruise(
    cruise_id,
    cruise_name,
    cruise_description,
    ship_code,
    cruise_departure_datetime,
    cruise_duration
)
VALUES(
    4,
    'Queensland Islands',
    '7 Night Queensland Islands Cruise. Start from Brisbane. Stops at Airlie Beach, Port Douglas, Cairns, Willis Island. Ends at Brisbane.',
    110,
    STR_TO_DATE(
        '07-May-2022 14:00',
        '%d-%b-%Y %H:%i'
    ),
    7
);

INSERT INTO cruise (
    cruise_id,
    cruise_name,
    cruise_description,
    ship_code,
    cruise_departure_datetime,
    cruise_duration
) VALUES (
    3,
    'New Zealand Delight',
    'Starts from Melbourne. Cruising in Fiordland National Park. Stops at Dunedin, Lyttelton (Christchurch), Wellington, Tauranga (Rotorua), Auckland. Ends at Melbourne.',
    103,
        STR_TO_DATE(
        '16-Apr-2022 9:00',
        '%d-%b-%Y %H:%i'
    ),
    13
);

INSERT INTO cruise(
    cruise_id,
    cruise_name,
    cruise_description,
    ship_code,
    cruise_departure_datetime,
    cruise_duration
)
VALUES(
    5,
    'Brisbane to Hobart',
    '7 nights at sea from Brisbane to Hobart.',
    104,
    STR_TO_DATE(
        '08-May-2022 10:30',
        '%d-%b-%Y %H:%i'
    ),
    7
);

INSERT INTO cruise(
    cruise_id,
    cruise_name,
    cruise_description,
    ship_code,
    cruise_departure_datetime,
    cruise_duration
)
VALUES(
    8,
    'Melbourne to Singapore',
    'Starts from Melbourne. Stops at Adelaide, Albany, Fremantle, Bali and Jakarta. Ends at Singapore.',
    105,
    STR_TO_DATE(
        '30-Oct-2022 9:30',
        '%d-%b-%Y %H:%i'
    ),
    24
);

INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(110, 1001, 4, 'I');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(110, 1002, 4, 'O');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(110, 2022, 2, 'B');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(110, 3001, 4, 'S');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(110, 3002, 4, 'S');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(102, 2001, 4, 'O');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(102, 2011, 4, 'I');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(102, 4002, 2, 'S');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(102, 4004, 2, 'S');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(102, 4033, 3, 'B');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(103, 110, 2, 'O');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(103, 211, 4, 'B');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(104, 142, 4, 'I');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(104, 211, 4, 'O');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(105, 8032, 3, 'O');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(105, 8033, 3, 'O');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(105, 9013, 2, 'B');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(105, 10101, 6, 'S');
INSERT INTO cabin(
    ship_code,
    cabin_no,
    cabin_capacity,
    cabin_class
)
VALUES(105, 10102, 4, 'S');


INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(105, 10102, 'Y');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(105, 10101, 'N');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(105, 9013, 'U');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(104, 142, 'Y');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(104, 211, 'N');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(103, 110, 'Y');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(103, 211, 'U');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(102, 4004, 'Y');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(102, 4002, 'U');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(102, 2011, 'N');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(110, 1002, 'Y');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(110, 2022, 'U');
INSERT INTO disable_cabin(
    ship_code,
    cabin_no,
    auxiliary_facilities
)
VALUES(110, 3001, 'N');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(110, 1001, 'N');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(110, 2022, 'Y');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(110, 3001, 'U');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(102, 2001, 'U');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(102, 2011, 'N');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(103, 110, 'U');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(103, 211, 'N');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(104, 142, 'Y');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(104, 211, 'N');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(105, 8033, 'U');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(105, 9013, 'N');
INSERT INTO smoking_cabin(
    ship_code,
    cabin_no,
    ashtrays
)
VALUES(105, 10101, 'Y');

INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    89,
    'Smith',
    'Jackson',
    STR_TO_DATE('07-Oct-1978', '%d-%b-%Y'),
    'M',
    '0411224509'
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    10,
    'Smith',
    'Harishi',
    STR_TO_DATE('10-Sep-2014', '%d-%b-%Y'),
    'F',
	NULL
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    87,
    'Luna',
    'Bob',
    STR_TO_DATE('10-Sep-1989', '%d-%b-%Y'),
    'M',
	'0411220912'
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    83,
    'Kevin',
    'Harry',
    STR_TO_DATE('10-Sep-1989', '%d-%b-%Y'),
    'M',
	'0411220756'
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    70,
    'Jack',
    'Frank',
    STR_TO_DATE('15-Sep-2011', '%d-%b-%Y'),
    'M',
	NULL
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    79,
    'Potter',
    'Lilly',
    STR_TO_DATE('27-Jun-1991', '%d-%b-%Y'),
    'M',
	'0411220196'
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    60,
    'Jesse',
    'Knight',
    STR_TO_DATE('15-Nov-2019', '%d-%b-%Y'),
    'F',
	NULL
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    74,
    'Herry',
    'Smith',
    STR_TO_DATE('27-Dec-1993', '%d-%b-%Y'),
    'F',
	'0411220023'
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    50,
    'Coco',
    'Mavry',
    STR_TO_DATE('15-Jan-2023', '%d-%b-%Y'),
    'F',
	NULL
);
INSERT INTO passenger (
    passenger_id,
    passenger_fname,
    passenger_lname,
    passenger_dob,
    passenger_gender,
    passenger_contact
) VALUES (
    65,
    'Chen',
    'Yao',
    STR_TO_DATE('27-Sep-1996', '%d-%b-%Y'),
    'F',
	'0411224104'
);

INSERT INTO manifest(
    manifest_id,
    passenger_id,
    cruise_id,
    manifest_board_datetime,
    ship_code,
    cabin_no
)
VALUES(1, 10, 2, NULL, 103, 110);
INSERT INTO manifest(
    manifest_id,
    passenger_id,
    cruise_id,
    manifest_board_datetime,
    ship_code,
    cabin_no
)
VALUES(
    2,
    89,
    4,
    '2022-05-07 09:00:00',
    STR_TO_DATE('07-May-2022 09:00', '%d-%b-%Y %H:%i'),
    110,
    1001
);
INSERT INTO manifest (
    manifest_id,
    passenger_id,
    cruise_id,
    manifest_board_datetime,
    ship_code,
    cabin_no
) VALUES (
    3,
    70,
    8,
    STR_TO_DATE('29-Oct-2022 22:30', '%d-%b-%Y %H:%i'),
    105,
    8032
);
INSERT INTO manifest (
    manifest_id,
    passenger_id,
    cruise_id,
    manifest_board_datetime,
    ship_code,
    cabin_no
) VALUES (
    4,
    50,
    3,
    STR_TO_DATE('15-Apr-2022 22:00', '%d-%b-%Y %H:%i'),
    103,
    211
);
INSERT INTO manifest (
    manifest_id,
    passenger_id,
    cruise_id,
    manifest_board_datetime,
    ship_code,
    cabin_no
) VALUES (
    5,
    79,
    4,
    STR_TO_DATE('07-May-2022 08:00', '%d-%b-%Y %H:%i'),
    110,
    2022
);




