CREATE TABLE IF NOT EXISTS Staff (
    staff_no CHAR(8) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    department CHAR(22) NOT NULL CHECK(department IN ("Catering", "Events Services", "Kitchen Staff", "Bar Services", "Facilities Management", "Audio and Visual", "Decor and Design", "Guest Services", "Security")),            
    PRIMARY KEY(staff_no)
)