CREATE TABLE IF NOT EXISTS Attend (
    FOREIGN KEY (bin) REFERENCES Banquet(bin),
    FOREIGN KEY (email_address) REFERENCES Attendee(email_address)
    PRIMARY KEY (bin, email_address),
)