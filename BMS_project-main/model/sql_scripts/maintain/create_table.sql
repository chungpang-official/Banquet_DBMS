CREATE TABLE IF NOT EXISTS Maintain (
    present BOOLEAN,
    FOREIGN KEY (bin) REFERENCES Banquet(bin),
    FOREIGN KEY (staff_no) REFERENCES Staff(staff_no),
    PRIMARY KEY (bin, staff_no)
)