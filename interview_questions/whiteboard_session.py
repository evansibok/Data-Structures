"""
*** BALANCE BRACKET PROBLEM ***

Write a function that takes a string as input. 
The string can contain three types of brackets: "[]", "()", "{}". 
Your function should return a boolean indicating whether or not the string is balanced.  
A string is considered balanced if it has as many opening brackets of a given type as it has closing brackets
of that same type. 
No bracket can be left unmatched if the string is to be considered balanced. 
A closing bracket also cannot match a corresponding opening bracket that comes after it. 
Brackets also cannot overlap each other, i.e., "[(])". 
"""
# Examples:
# "[(])" should return false
# "foo(bar)baz" should return true
# "{{[]}}" should return true
# "I am happy to take your donation; any amount will be greatly appreciated." should return true
# "I (wa)n{t to buy a on}esie[…] b(u{[t] kno}w it) won't suit me." should return true
# "This is t(he la[st random sentence I will be writing and I am going to stop mid-sent]" should return false


# It takes a string as an input
# Can contain three bracket types
# Should return true if the string is balanced (should
# have at least an opening and closing bracket of the same type) otherwise return false
# ][ is invalid
# [(]) (There has to a value in between each bracket)


# "[{let}]" - balanced
# "[{}]" - balanced
# "" - balanced
# "][{}" - unbalanced
# "[}" - unbalanced
# "]" - unbalanced
# {[}]

# "{dkigo}"
# "dhdif}dkigo{"
# "{jdldp[dld]}"

# {
#     "[": "]",
#     "{": "}",
#     "(": ")",
# }

l = ["{", "[", "]", "}"] = "{[]}"

l = ["{", "[", "}", "]"] = "{[}]"

l = ["{", "}", "[", "]"] = "{}[]"

# We may not have to find every string
# We can pop from l and if the char at next index is not a corresponding
# closing bracket or is


# Base case
# if len(l) is 0 return True


# if the length of this list is not even, return False
# otherwise
# run through the list
#
# If the value at the current index matches the key at dictionary
# and the value at the current index + 1 matches the value property in the dictionary
#
# else
#


# ob = ["{", "["]
# cb = ["]", "}"]


# Base Case - If we get an empty string, end & return True

# If it is not a string, return False
# If we get a string, run through the string
# compare the character at the current index to the character at the next index
# if the first identifiable character at the current index is a closing bracket, it should return False
# otherwise
# if the first identifiable character at the current index matches any of the keys in the dictionary (opening brackets) continue
# push the character to a list
# for every identifiable character
# if the character matches the key in the dictionary save to the opening bracket list
# else if the character matches the value in the dictionary save to the closing bracket list
# otherwise return false

# PSEuDOCODE
# if input is not a string, return false
# if input is equal to an empty string return true
# otherwise
# check the string characters
# if the character from the string equals the key from the dictionary
#


# -------------------------------
# Declare an empty list
# Create a dictionary that hold's the opening bracket as key and closing bracket as equivalent value
# Create another dictionary that
