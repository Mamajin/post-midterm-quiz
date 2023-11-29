1. Created a class for the csv to table converter of ease of use
2. Updated the Table class with new methods insert_row and update_row
3. Created an object for the csv class
4. Created DB object 
5. Created a Table object table1 to store the table converted from the csv object
6. Insert the table into my_DB
7. Using the filter method to create a new table with the desired key value and aggregate 
   methods to get the total Gross, achieve the average Gross of comedy movies then print the result
8. Find the min score for Drama movies by using the filter to sort the table to
   only have the value of the key 'Genre' to have only 'Drama' then use the 
   aggregate method to get the min value
9. Filter table1 to only have the key value of 'Genre' be 'Fantasy' then use
   aggregate method to find the len(x) of the new table1
10. Add the new movie with the new insert_row method
11. Call the same functions as 9. but now the number of 'Fantasy' movies will change
12. Update the film 'a serious man' with the new method update_row to change the 
    value of 'Year' to 2022
