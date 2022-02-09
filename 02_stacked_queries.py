# 2. Stacked Queries
"""
You have an empty stack. You will receive an integer – N.
On the next N lines, you will receive queries.
Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
"""

num_integers = int(input())
stack_to_fill = []

for el in range(num_integers):
    data = [int(x) for x in input().split()]
    if data[0] == 1:
        stack_to_fill.append(data[1])

    elif data[0] == 2:
        stack_to_fill.pop()
    elif data[0] == 3:
        print(max(stack_to_fill))
    elif data[0] == 4:
        print(min(stack_to_fill))

while stack_to_fill:
    el = stack_to_fill.pop()
    if stack_to_fill:
        print(el, end=", ")
    else:
        print(el)
