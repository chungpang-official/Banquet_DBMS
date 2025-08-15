CREATE TABLE IF NOT EXISTS Provide {
    FOREIGN KEY(bin) REFERENCES Banquet(bin)
    FOREIGN KEY(meal_no) REFERENCES Meal(meal_no)
    PRIMARY KEY(bin, meal_no),
}