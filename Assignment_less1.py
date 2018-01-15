
# coding: utf-8

# In[5]:


# first program in jupyter notebook

print("Welcome to Python")


# In[2]:


# Create a list based on some conditions

num= range(2000,3200)
l=[]
for i in num:
    if i%7 == 0 and i%5 != 0:
       l.append(i)
print(l)




# In[3]:


# Get first and last name and print in reverse

first_nm = input("Enter your first name")
last_nm= input("Enter your last name")
print(last_nm, first_nm)


# In[1]:


# Calculate volume of a sphere

diameter = 12
radius=diameter/2
pi = 3.14

Vol = 4/3 * pi * radius**3

print("Volume of sphere is", Vol)

