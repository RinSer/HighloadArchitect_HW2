CREATE INDEX idx_first_and_second_name
    USING BTREE
    ON profiles (firstName, secondName);