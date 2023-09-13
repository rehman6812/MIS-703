#!/usr/bin/env python
# coding: utf-8

# In[15]:


x = 5 
print('Hello')

def print_lyrics(): 
 print("I'm a lumberjack, and I'm okay.") 
 print('I sleep all night and I work all day.')

 print('Yo')

x = x + 2

print(x)


# In[16]:


def greet(): return "Hello"

print (greet(), "Glenn") 
print (greet(), "Sally")


# In[33]:


def greet (lang):

 if lang == 'es': 

  return 'Hola'
 elif lang == 'fr': 
    return 'Bonjour'

 else:
   return 'Hello'

print(greet('en'), 'Glenn')

Hello Glenn

print(greet('es'), 'Sally')

Hola Sally

print(greet('fr'), 'Michael')

Bonjour Michael




# In[ ]:


def computepay(hours, rate):
    return hours * rate

regular_rate = float(input("Hourly rate in dollars: "))
regular_hours = float(input("Regular hours worked: "))
overtime_hours = float(input("Overtime hours worked: "))

regular_pay = computepay(regular_hours, regular_rate)
overtime_pay = computepay(overtime_hours, regular_rate * 1.5)
total_pay = regular_pay + overtime_pay

print(f"This pay period you earned: ${total_pay:.2f}")


# In[ ]:




