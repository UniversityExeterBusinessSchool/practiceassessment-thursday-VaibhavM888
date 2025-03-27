#######################################################################################################################################################
# 
# Name:Vaibhav Maheshwari
# SID:750018329
# Exam Date:27/01/2022
# Module:BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-VaibhavM888
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()


# Question 1 - Answer 
# Initializing empty list to store the (start, end) locations 
my_list = []

# My allocated keys are 7 and 9 and words are 'resolve' and 'minor'
my_SID_keys = [7, 9]

# Iterating through the allocated keys
for key in my_SID_keys:
    # to get the word corresponding to the key (7: resolve & 9:minor) from the dictionary
    SID_keyword = key_comments[key]
    
    # To find the starting location of the word in the customer_feedback string
    starting_location = customer_feedback.find(SID_keyword)
    
    # If statement to find word and calculate the end location
    if starting_location != -1:
        end_location = starting_location + len(SID_keyword) - 1  # End location is start + length of word - 1 because it  starts from zero
        # Append the tuple (start, end) to my_list
        my_list.append((starting_location, end_location))

# Print result
print("List of (start, end) positions:", my_list)

#Question 2 - Answer
# First two digits of my ID number: 75
# Last two digits of my ID number: 29

# Operating Profit Margin = (Operating Profit / Revenue) * 100
def calculate_operating_profit_margin(revenue, operating_profit):
    if revenue == 0:  # to avoid division by zero and error
        return "Revenue cannot be zero."
    return (operating_profit / revenue) * 100

# Revenue per Customer = Total Revenue / Total Customers
def calculate_revenue_per_customer(total_revenue, total_customers):
    if total_customers == 0:  # To avoid division by zero and error
        return "Total customers cannot be zero."
    return total_revenue / total_customers

# Function to calculate Customer Churn Rate = (Customers Lost / Total Customers) * 100
def calculate_customer_churn_rate(customers_lost, total_customers):
    if total_customers == 0:  # To avoid division by zero and error
        return "Total customers cannot be zero."
    return (customers_lost / total_customers) * 100

# Function to calculate Average Order Value = Total Revenue / Total Orders
def calculate_average_order_value(total_revenue, total_orders):
    if total_orders == 0:  # to avoid division by zero and error
        return "Total orders cannot be zero."
    return total_revenue / total_orders

# Input Values using my ID digits 
revenue = 75  # Input Values of revenue based on ID first two digits (75) because revenue !< operating profit
operating_profit = 29  # Input Values of revenue based on ID last two digits
total_customers = 8  # Total customers rounding off 7.5 to 8
customers_lost = 3  # Customers lost rounding off 2.9 to 3
total_orders = 10  # Total orders let say 10

# Results
operating_profit_margin = calculate_operating_profit_margin(revenue, operating_profit)
print("Operating Profit Margin:", operating_profit_margin, "%") # % sign added to show percentage

revenue_per_customer = calculate_revenue_per_customer(revenue, total_customers)
print("Revenue per Customer:", revenue_per_customer) 

customer_churn_rate = calculate_customer_churn_rate(customers_lost, total_customers)
print("Customer Churn Rate:", customer_churn_rate, "%") # % sign added to show percentage

average_order_value = calculate_average_order_value(revenue, total_orders)
print("Average Order Value:", average_order_value)

Question 3 - Answer
import numpy as np
from scipy.stats import linregress

# Data: Price and Demand
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])  # Prices are in £
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])  # Demand in units

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(prices, demand)

# Calculate demand for a given price
def cal_demand(price):
    return slope * price + intercept

# Calculate revenue for a given price
def cal_revenue(price):
    return price * cal_demand(price)

# 1. Find the price that maximizes revenue
# Prices in the range of 20 to 70 (inclusive)
test_prices = np.arange(20, 71)  # Generate prices from 20 to 70
revenues = [cal_revenue(price) for price in test_prices]
max_revenue_price = test_prices[np.argmax(revenues)]  # Price with maximum revenue

# 2. Find the demand when the price is set at £52
demand_at_52 = cal_demand(52)

# Results
print("Price that maximizes revenue: £", max_revenue_price)
print("Demand when price is set at £52:", demand_at_52)
