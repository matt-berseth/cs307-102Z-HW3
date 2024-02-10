"""
Objective:
Write a Python program that encodes a sequence of numbers based on specific rules. 
The program should ask the user for a sequence of numbers and then apply a
transformation to each number in the sequence according to defined criteria.

Requirements

User Input:
Prompt the user to enter a sequence of integers separated by spaces (e.g., "1 2 3 4 5").

Encoding Rules:
For each number in the sequence:
- If the number is less than 5, multiply it by 2.
- Else if the number is equal to 5, then subtract 1 from it.
- Else if the number is greater than or equal to 7 and less than to 14, then set it equal to zero
- Otherwise, just return the number

Output the Encoded Sequence:
Display the transformed sequence as a series of numbers separated by spaces.

Example:
User Input: 1 2 3 4 5
Output: 2 4 6 8 4
"""

def transform_sequence(string_input):
   outputs = []

   # TODO, your logic needs to go here.
   # it will include a for loop to iterate over the input provided
   # by the user. It is safe to assume the input string is formatted properly
   # i.e. integers seperated by a space.

   # join the items in the outputs list together with a space.
   return " ".join(outputs)



test_input = "1 2 3 4 5"
print(f"Running test 1 with string: '{test_input}'")
# transform the values and evaluate the results
test_output = transform_sequence(test_input)
expected_output = "2 4 6 8 4"
if test_output == expected_output:
   print("PASS")
else:
   print(f"FAILED, expected: {expected_output} actual: {test_output}")


test_input = "12 19 17 0 9"
print(f"Running test 2 with string: '{test_input}'")
# transform the values and evaluate the results
test_output = transform_sequence(test_input)
expected_output = "0 19 17 0 0"
if test_output == expected_output:
   print("PASS")
else:
   print(f"FAILED, expected: {expected_output} actual: {test_output}")


test_input = "14 7 19 7 10"
print(f"Running test 3 with string: '{test_input}'")
# transform the values and evaluate the results
test_output = transform_sequence(test_input)
expected_output = "14 0 19 0 0"
if test_output == expected_output:
   print("PASS")
else:
   print(f"FAILED, expected: {expected_output} actual: {test_output}")


test_input = "3 9 1 2 17"
print(f"Running test 3 with string: '{test_input}'")
# transform the values and evaluate the results
test_output = transform_sequence(test_input)
expected_output = "6 0 2 4 17"
if test_output == expected_output:
   print("PASS")
else:
   print(f"FAILED, expected: {expected_output} actual: {test_output}")
