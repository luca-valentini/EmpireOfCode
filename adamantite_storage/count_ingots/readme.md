#Count Ingots

To create an accurate accounting of our stock, incoming ingots in cargo shipments are numbered.

Ingots in each consignment are numbered in the row from A1 to Z9 as A1, A2,..., A9, B1, B2, ..., Z9. Each consignment is marked with the number of the last ingot in it. So you can define the quantity of ingots by the number of marks.

You are given a report of daily consignments as number marks written in a string separated by commas. Count the total quantity of ingots. Take the report "A2,B1" for example. Here we can see two consignments with 2 (A2) and 10 (B1) ingots, giving us a result of 12.

###Input:
A daily report as a string.

###Output:
The total quantity of ingots as an integer.

###Example:
```javascript
count_ingots("A2,B1") == 12
count_ingots("A1,A1,A1") == 3
count_ingots("Z9,X8,Y7") == 672
count_ingots("C1,D1,B1,E1,F1") == 140
```
###Precondition:

report match with regexp expression "[A-Z][1-9](,[A-Z][1-9])*"

###How it is used:

This concept uses a modified numeral system and provides you with a basis for working with strings.
