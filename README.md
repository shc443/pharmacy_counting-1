Used Language : Python 3

Required Library : csv, sys, os

First I transformed the data into the lists of list, and I appended each id into the list(pre) if it has not been appended before. 
Then I summed the total cost and the number of id for each drug by creating a dictionary. 
At last, I sorted the dictionary based on the total cost in descending order. (Ascending drug name order if there is a tie)

I had to add some unnecessary lines because of one bug in the check repo link; "line[3]" part arose "IndexError: list index out of range" error even though "line" is a list of 5 items. 
