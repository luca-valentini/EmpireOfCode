#Three Words

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in **succession**. For example, the string "start 5 **one two three** 7 end" contains three words in succession.

###Input
A string with words.

###Output
The answer as a boolean.

###Example
```javascript
three_words("Hello World hello") == True
three_words("He is 123 man") == False
three_words("1 2 3 4") == False
three_words("bla bla bla bla") == True
three_words("Hi") == False
```

###Precondition

The input contains words and/or numbers. There are no mixed words (letters and digits combined).

	0 < |words| < 100

###How it is used

This teaches you how to work with strings and introduces some useful functions.
