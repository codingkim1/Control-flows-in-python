#Define a function that determines whether a given string is a Palindrome.

#A normal python function to determine a palindrome of a given string 
def isPalindrome(string):
    if (string == string[::-1]):
        return 'A Palindrome'
    else:
        return 'Not A Palindrome'
    
#enter input string
string = input()
 
print(isPalindrome(string))
 
    
