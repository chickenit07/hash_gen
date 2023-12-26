### SUMMARY
I made this script to help auto generate the hash (MD5 and SHA256).

### HOW IT WORKS
1. The script takes username and timestamp from the input file line by line.
2. Combine those 2 elements with one of every special characters to a list.
3. Then randomly shuffle the 3 components.
4. Hash the results with md5 and sha256.

### EXAMPLE
The input file input.txt should contains 2 lines like below: 

username
timestamp

$python3 hash_gen.py input.txt
