# 7. ?
# DELETE from shopping WHERE name like 'Orange';
# delete function here is used to delete all row completely from the shopping table where name is "orange"

# 8. ?
# UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
# UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'
# the update function in first instance is used to change name to "bisli" where name is set to "bamba"
# in second instance the update function is used to change the amount of product from the shopping table by name "milk" to 1

# 9. ?
# ALTER TABLE shopping ADD COLUMN maavar
# alter function here is used to add a column called "maavar" to all rows in the shopping table

# 10. ?
# UPDATE shopping SET maavar=6 WHERE id=1;
# UPDATE shopping SET maavar=3 WHERE id=2;
# UPDATE shopping SET maavar=12 WHERE id=3;
# UPDATE shopping SET maavar=8 WHERE id=4;
# UPDATE shopping SET maavar=5 WHERE id=5;
# the update function here is used to add value to the "maavar" column in each row using condition to append given value to correct row

# 11. ?
# SELECT * FROM shopping WHERE amount > 1 AND maavar > 5
# SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5
# the select function here is used to print only rows where amount of product is bigger than 1 and the maavar of that product is bigger than 5
# in the second instance the select function is used to print only the rows where maavar column value is between 3 and 5

# 12. ?
# SELECT * FROM shopping ORDER BY maavar
# SELECT * FROM shopping ORDER BY maavar DESC
# the select function here is used to print all rows in ascending order which sorted by "maavar" column value
# in second instance is the same but rows sorted by "maavar" in descendant order instead

# 13. ?
# CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
# INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
# INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
# DELETE FROM books;
# create function here is used to create a new table by name "books" which has two key parameters (id and name)
# then you have two insert functions that used to make two new rows with values of (id and name)
# delete function here is used to delete all rows from the "books" table

# 14. ?
# SELECT COUNT(*)from shopping
# SELECT MAX(amount) from shopping
# SELECT AVG(amount) from shopping
# SELECT MIN(amount) from shopping
# count used to count and print the amount of rows in the "shopping" table
# max is used to print the biggest value of the amount key in the shopping table
# avg is used to print the average of the amount key in the shopping table by dividing the sum of all amount values from all rows by their count
# min is used to print the smallest value of the amount key in the shopping table

# 15. ?
# INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
# INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
# Select maavar, COUNT(*)FROM shopping GROUP BY maavar
# insert function here is used to insert two more rows to the shopping table by adding values to given keys
# the problem in the first insert is that id number 6 is already taken
# the select function here is used to print two rows one for "maavar" column and second for count that counts how many times given maavar value is repeated in this table all of this is sorted by ascending order of the maavar value

# 16. ?
# SELECT id AS "SECRET", name, amount, maavar FROM shopping
# in this function "id" key name changed to "secret" in the print of the "shopping" table
