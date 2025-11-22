1. Program to print the Fibonacci sequence. 

```python
n = int(input("Enter a number:"))
a , b = 0 , 1
for _ in range(n):
    print(a , end="\n")
    a , b = b , a + b 
```



2 . Program to Make a Simple Calculator.

```python

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

msgs = \
"""
Choose a option 
1. add
2. sub
3. multiply
4. Divide
5. exit 
"""
print(msgs)
user_choose = int(input("Enter a opertion For continue: "))
numb1 = int(input("Enter the first Number:"))
numb2 = int(input("Enter the Second Number:"))

while True:
    if user_choose == 1:
        print(add(numb1,numb2))
    elif user_choose == 2:
        print(sub(numb1,numb2))
    elif user_choose == 3:  
        print(mul(numb1,numb2))
    elif user_choose == 4:
        print(div(numb1,numb2))
    break
else:
    print("Invalid Operation")

```




3. Program to Take in the Marks of 5 Subjects and Display the Grade .

```python
sub1 = int(input("Enter 1 mark: "))
sub2 = int(input("Enter 2 mark: "))
sub3 = int(input("Enter 3 mark: "))
sub4 = int(input("Enter 4 mark: "))
sub5 = int(input("Enter 5 mark: "))

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if (avg >= 90):
    grade = "A" 
elif (avg >= 80 and avg < 90):
    grade = "B"
elif (avg >= 70 and avg < 80):
    grade = "C"
elif (avg >= 60 and avg < 70):
    grade = "D"
else:
    grade = "F"

print("Grade :", grade)




4. Program to check if a Number is a Palindrome. 

n = int(input("Enter a number: "))
temp , rev = n , 0
while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if (temp == rev):
    print("Number is a Palindrome.")
else:
    print("Not Number is a Palindrome.")

```



5. Program to find Factorial of a number. 
```python
def Factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact

num = int(input("Enter the Number: "))
print("Factorial of", num, "is", Factorial(num))
```



6. Read Two Numbers and Print Their Quotient and Remainder.
```python
quotient = lambda a, b: a // b
remainder = lambda a, b: a % b
print("Quotient:", quotient(10, 3))
print("Remainder:", remainder(10, 3))
```

7. Add two matrices using nested loop.
```python
x = [[12,7,3],
     [4,5,6],
    [7,8,9]]
y = [[5,8,1],
     [6,7,3],
     [4,5,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
            result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)

```
8.  Program to sort alphabetically the words from a string provided by the user.
```python
my_str = "Hello this is an Example with cased letters"
word = [word.lower() for word in my_str.split()]
word.sort()
print("The sorted words are:")

for w in word:
    print(w)
```
9. Multiply two matrices using nested loops.
```python
x = [[12,7,3],
     [4,5,6],
    [7,8,9]]
y = [[5,8,1],
     [6,7,3],
     [4,5,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
for r in result:
    print(r)
```
10. Program to check if a year is a leap year or not.
```python 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):    
 print("Leap Year")
else:
 print("Not a Leap Year")  
  
```  


11.  Matrix Transpose using Nested Loop.
```python
x =  [[1,2],[4,5],[7,8]]
result = [[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
         result[j][i] = x[i][j]
for r in result:
    print(r)
```

12. Program to count the number of each vowels.

```python 
vowels = "aeiou"
str = "Hello , have you tried"
str = str.casefold()
count={}.fromkeys(vowels,0)
for char in str:
 if char in count:
  count[char] += 1
print(count)
```

13. Program to display all Prime numbers within an interval. 
```python 
lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
```
14.  Program to solve Quadratic equation. 
```python
import cmath
a = float(input("Enter a "))
b = float(input("Enter b "))
c = float(input("Enter c "))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
```
15. Program to display Fibonacci Sequence Using Recursion.
```
def recr_fibo(n):
    if n <= 1:
        return n
    else:
        return recr_fibo(n - 1) + recr_fibo(n - 2)
    

    
nterms = int(input("Enter the number of terms: "))
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Series:")
    for i in range(nterms):
        print(recr_fibo(i))

```