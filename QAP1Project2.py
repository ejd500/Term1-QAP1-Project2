# Description:      This program calculates and breaks down the cost of renting
#                   a car at Edsel Car Rental Company
# Author:           Ellen Dalton
# Date Started:     May 8, 2023
# Date Completed:   May 8, 2023

# Constants are as follows:
RATE_PER_DAY = 55.00
RATE_PER_KM = 0.24
HST_RATE = 0.15

# Input the following:
print("Please enter the following: ")
cus_name = input("Customers Name: ")
phone_num = input("Phone Number: ")
num_days_rented = float(input("The number of days the car was rented: "))
mileage_when_rented = float(input("The mileage when the car was rented: "))
mileage_when_returned = float(input("The mileage when the car was returned: "))

# Calculate the following:
tot_km = float(mileage_when_returned - mileage_when_rented)  # total number of kilometers travelled
cost_of_rental = float((RATE_PER_DAY * num_days_rented) + (RATE_PER_KM * tot_km))  # Subtotal = daily_cost + mile_cost
sales_tax = float(HST_RATE * (RATE_PER_DAY * num_days_rented))  # HST on the daily cost only
tot_rental_cost = float(cost_of_rental + sales_tax)  # Total rental cost including sales tax

# Display the following:
print()
print(f"Customer's Name: {cus_name:<20s}")
print(f"Phone Number:    {phone_num:<20s}")
print()
print(f"The number of days the car was rented:    {num_days_rented:>12.1f}")
print(f"The mileage when the car was rented:      {mileage_when_rented:>12.1f}")
print(f"The mileage when the car was returned:    {mileage_when_returned:>12.1f}")
print(f"Total number of kilometers travelled:     {tot_km:>12.1f}")
print()
print(f"Subtotal (i.e. the cost for the rental): ${cost_of_rental:>12.2f}")
print(f"HST (i.e on the daily cost only):        ${sales_tax:>12.2f}")
print(f"Total Rental Cost:                       ${tot_rental_cost:>12.2f}")
print()
