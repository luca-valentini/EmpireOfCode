#Place Queens

Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. Ancient humans loved this game of skill and strategy and our Robots are attempting to examine all tricks to becoming True Scientist. Today they are trying to solve the 8-Queen problem as written in an old chess-manuscript.

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with Queens. The Queen can move any number of squares along the rank, file, or diagonal axis.

You should place eight chess Queens on an 8×8 chessboard so that no two Queens threaten each other. For this challenge, we have already placed one or more Queens on the board, so you will need to finish the placement. In addition, each Queen may be considered as part of it’s army, meaning every Queen could possible be a threat to every other Queen on the board.

You are given a set of square coordinates where we have placed Queens already. You should finish this set and return the full set of the coordinates for all eight Queens. If it's not possible -- return an empty set. Be careful - an initial position could possibly threaten another Queen right off the bat.

###Input: Placed Queens coordinates as a set of strings.

###Output: Eight Queens coordinates as a set of strings or an empty set.

###Example:
```javascript
place_queens({"b2", "c4", "d6", "e8"})  # {"b2", "c4", "d6", "e8", "a5", "f3", "g1", "h7"}
place_queens({"b2", "c4", "d6", "e8", "a7", "g5"}) == set()
```
###Precondition:

An input strings satisfies regexp "[a-h][1-8]".

0 < |placed| < 8

###How it is used:

This is a classical puzzle and combinatorial constraints problem. It can be useful if you need make a schedule for teachers and classes, or for sport games occurring in several different stadiums.
