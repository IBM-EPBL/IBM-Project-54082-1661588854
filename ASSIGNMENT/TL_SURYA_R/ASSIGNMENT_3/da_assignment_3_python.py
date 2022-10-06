# -*- coding: utf-8 -*-
"""DA_Assignment_3_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HTEE_O__VGdjGOKaCOSVdoZwjzkUUSd1

## Exercises

Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

** What is 7 to the power of 4?**
"""

7 ** 4

"""** Split this string:**

    s = "Hi there Sam!"
    
**into a list. **
"""

s = "Hi there Sam!"
s.split()

"""** Given the variables:**

    planet = "Earth"
    diameter = 12742

** Use .format() to print the following string: **

    The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet,diameter))

"""** Given this nested list, use indexing to grab the word "hello" **"""

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2][0]

"""** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d['k1'][3]['tricky'][3]['target'][3]

"""** What is the main difference between a tuple and a list? **"""

#Tuple is immutable where list is mutable

"""** Create a function that grabs the email website domain from a string in the form: **

    user@domain.com
    
**So for example, passing "user@domain.com" would return: domain.com**
"""

def domainGet(email):
    return email.split('@')[-1]

domainGet('user@domain.com')

"""** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **"""

def findDog(st):
    return 'dog' in st.lower().split()

findDog('Is there a dog here?')

"""** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **"""

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count

countDog('This dog runs faster than the other dog dude!')

"""### Problem
**You are driving a little too fast, and a police officer stops you. Write a function
  to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
  If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
  and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
  cases. **
"""

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

caught_speeding(81,False)

caught_speeding(70,True)

"""Create an employee list with basic salary values(at least 5 values for 5 employees)  and using a for loop retreive each employee salary and calculate total salary expenditure. """

employee = [30000,23000,25000,40000,33000]
tot = 0
for i in employee:
    tot = tot + i
print("Total Salary :",tot)

"""Create two dictionaries in Python:

First one to contain fields as Empid,  Empname,  Basicpay

Second dictionary to contain fields as DeptName,  DeptId.

Combine both dictionaries. 
"""

dict1 = {
    "EmpId":[1001,1002,1003,1004],
    "EmpName":["Surya.R","Surya.K","Subash.M","Keshav.J"],
    "Basicpay":[45000,42000,43000,44000]
}

dict2 = {
    "DeptName":["CSE","ECE","EEE","IT"],
    "DeptId":["19CS","19ECE","19EEE","19IT"]
}

dict1.update(dict2)
dict3 = dict1.copy()
dict3