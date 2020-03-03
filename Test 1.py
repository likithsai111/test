#!/usr/bin/env python
# coding: utf-8

# # Practice Assessment
# This is your first assessment. Although it is for practice only, you must go through each question and ensure you can  run your Python code in the notebook. 
# 
# It is important that you are able to save your completed notebook into a repo in your GitHub account. And you must be able to email a copy of your uploaded file to james.connolly@lyit.ie 

# ## Q1
# Using an f-string, display this Einstein quote exactly as you see it. 
# 
# Anyone who has never made a mistake <br>
#          has never tried anything new.

# In[16]:


print(f"Anyone who has never made a mistake \n has never tried anything new")


# ### Q2 
# Using an f-string and the variables provided, display this message
# 
# `Letterkenny Institute of Technology can be abbreviated to (LYIT).`

# In[13]:


LYIT_name = "Letterkenny Institute of Technology"
acronym = "LYIT"

# Enter your code here
print(f"{LYIT_name} can be abbreviated to {acronym}")


# ### Q3
# Write a Python program to display the current date and time.
# 
# Sample output:
# `2020-01-10 18:31:21.076466`

# In[2]:


import datetime
today = datetime.datetime.today() 
print(f"{today:%B %d, %Y}") 


# ### Q4
# Write a Python program to ask the user to input their first name and DOB. Then calculate the number of days they have been alive.
# 
# Display a message to the user with an f-string using this format `James, you are 40 years old`.
# 
# Use the following code and then add your code.

# In[19]:


import datetime as dt
print(dt.date.today())

first_name = input("Please enter your first name : ")
print("Please enter your DOB as integer values")
year = int(input("Enter year : "))
month = int(input("Enter month : "))
day = int(input("Enter day : "))
  
birthdate = dt.date(year, month, day)
today = dt.date.today()
age = (today - birthdate)
days_old = age.days
years_old = days_old // 365
print(f"{first_name}, you are {years_old} years old")


# ### Q5
# Enter 2 numbers. If both numbers add up to a number between 50 to 60 then print a message stating `not accepted`, otherwise show a message `accepted`. 
# 
# Hint: Use the `sum in range` command to check whether your number is within a specific rang or not.

# In[20]:


number1 = int(input("Please enter number 1 : "))
number2 = int(input("Please enter number 2 : "))
sum = number1 + number2
if sum in range(50, 60):
    print('not accepted')
else:
    print('accepted')
  


# ### Q6
# Write a Python program to calculate the hypotenuse of a right angled triangle.
# 
# Hint : hytothenuse = square root of 2 shortest sides squared

# In[17]:


from math import sqrt
print("Input lengths of shorter triangle sides : ")
a = float(input(" side a: "))
b = float(input(" side b: "))
c = sqrt (a**2 + b**2)
print(c)


# ### Q7
# Use PyPDF2 to open the file **A_Midsummer_Night**. Extract the text of page 22 from this pdf. Print the contents of it.

# In[41]:



import PyPDF2
my_pdf_file = open("A_Midsummer_Night.pdf", mode="rb")
pdf_reader = PyPDF2.PdfFileReader(my_pdf_file)
pdf_page = pdf_reader.getPage(21).extractText()
print(pdf_page)


# ### Q8
# Open a new file called **OnePage.txt** and add the text you extracted from page 22 from the pdf file **A Midsummer Night** into the file **OnePage.txt**.

# In[9]:





# ### Q9
# Now print the contents of **OnePage.txt**. Store the contents of the file in a variable called **file_contents**.

# In[10]:





# ### Q10
# Using the **file_contents** variable above, extract any text that is 5 characters long followed by an exclamation mark.

# In[11]:





# ### Save your file to GitHub
# 
# Create a repo called **AI assessments** and save this assessment file to it.
# 
# Email a link to your GitHub page to james.connolly@lyit.ie
