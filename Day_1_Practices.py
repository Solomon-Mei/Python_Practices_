"""
Question 1
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

# My Solution

S = ""
i: int
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        S = S + str(i) + ','
print(S)

# Main author's Solution 1

# l = []
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         l.append(str(i))
#
# print(','.join(l))
#
#
# # Main author's Solution 2
#
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=',')
# print("\b")  # "\b" means backspace, it will cancel the last comma.

"""
Question 2
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""

# My solution
f = 1
for i in range(1, int(input("factorial number:")) + 1):
    f = f * i
print(f)

# Solution 1: Using While Loop

# n = int(input()) #input() function takes input as string type
#                  #int() converts it to integer type
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i = i + 1
# print(fact)

# Solution 2: Using For Loop

# n = int(input()) #input() function takes input as string type
#                 #int() converts it to integer type
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# Solution 3: Using Lambda Function

# Solution by:  harshraj22

# n = int(input())
# def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
# print(shortFact(n))


"""
With a given integral number n,
write a program to generate a dictionary that contains (i, i x i) 
such that is an integral number between 1 and n (both included).
and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

# My solution
D = []
n = int(input("Dictionary:"))
for i in range(1, n + 1):
    d = [i, i * i]
    D.append(d)
print(dict(D))

# Solution 1: Using For Loop

# n = int(input())
# ans = {}
# for i in range (1,n+1):
#     ans[i] = i * i
# print(ans[1])

# Solution 2: Using dictionary comprehension
# n = int(input())
# ans={i : i*i for i in range(1,n+1)}
# print(ans)
