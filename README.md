#Tubes SA

anggota :

1. Ricky
2. Vio
3. Clinton

Explaining :

1. Brute Force Method
   What It Does:
   The brute force method checks all possible substrings of the given string to see if they are palindromes. It does this by iterating over all pairs of starting and ending indices in the string and for each pair, it checks if the substring is the same forwards and backwards.

How It Works:

Double Loop: There are two nested loops. The outer loop selects the start index of the substring, and the inner loop selects the end index.
Palindrome Check: For each substring determined by the start and end indices, the code checks if it reads the same forwards and backwards.
Tracking the Longest: If a palindrome is found and its length is greater than the current maximum length recorded, update the maximum length and note the starting position of this substring.
Complexity: O(n^3). This is because checking each substring for being a palindrome takes O(n) and there are O(n^2) substrings.

2. Dynamic Programming
   What It Does:
   This method uses a 2D table where the entry at table[i][j] is True if the substring from index i to j is a palindrome. It builds this table by considering increasingly longer substrings and using the results of shorter substrings to determine if the longer ones are palindromes.

How It Works:

Initialize for Length 1: All substrings of length 1 are palindromes.
Check for Length 2: Substrings of length 2 are palindromes if both characters are the same.
General Case: For substrings longer than 2, use the relation that s[i] to s[j] is a palindrome if s[i] == s[j] and s[i+1] to s[j-1] is also a palindrome.
Update: For each found palindrome, if its length is the longest found so far, update the best starting position and length.
Complexity: O(n^2). The table has n^2 entries, and each entry requires constant time to compute with the precomputed results.
