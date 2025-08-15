CREATE TABLE IF NOT EXISTS Attendee (
    email_address VARCHAR(50) NOT NULL CHECK(email_address LIKE "%@%"),
    password VARCHAR(20) NOT NULL , -- ON UPDATE RESTRICT
    first_name VARCHAR(20) NOT NULL CHECK(first_name REGEXP '^[A-Za-z]+$'),
    last_name VARCHAR(20) NOT NULL CHECK(last_name REGEXP '^[A-Za-z]+$'),
    type CHAR(7) NOT NULL CHECK(type IN ("Staff", "Student", "Alumni", "Guest")),
    phone_no CHAR(8) NOT NULL CHECK(LENGTH(phone_no) = 8 AND phone_no NOT LIKE '% '),
    address VARCHAR(255) NOT NULL,
    organization VARCHAR(40) NOT NULL,
    PRIMARY KEY(email_address)
)
