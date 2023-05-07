# Name: Ben Hill
# Date: 5/6/2023

from cgitb import small
from ArrayList import ArrayList
from Client import Client
from Quicksort import Quicksort
from datetime import date
import time
import random
import sys

# display name and date in output
print("Name: ", "Ben Hill")
print("Date: ", date.today())
print()

clients = []

input_file_name = 'ClientData.csv'
with open(input_file_name) as file:
    for line in file:
        sep_by_comma = line.split(',')
        client_id = int(sep_by_comma[0]) # convert string to int
        f_name = sep_by_comma[1]
        l_name = sep_by_comma[2]
        phone = sep_by_comma[3]
        email = sep_by_comma[4]

        # create client objects with data file
        clt = Client(client_id, f_name, l_name, phone, email)

        clients.append(clt)

# sort the client data
Quicksort.sort(clients)

# how many client objects do we have?
num_records = len(clients)
my_array_list = ArrayList()

# Scenario 1: Printer Queue or Call Queue
section_title = "Scenario: Printer Queue or a Call Queue"
print(section_title)
print("-" * len(section_title))

# calculates time it would take adding client records to ArrayList
start_time = time.time()

for i in range(num_records):
    my_array_list.append(clients[i])

end_time = time.time()
total_time = end_time - start_time
print(f"\nIt took {total_time:.6f} seconds to add records!")

# how long does it take to remove records from the front of the ArrayList?
start_time = time.time()

for i in range(num_records):
    my_array_list.remove_at(0)

end_time = time.time()
total_time = end_time - start_time
print(f"\nIt took {total_time:.6f} seconds to remove records!")


# Scenario 2: Customer service center
answer = input("\nContinue (y/n)?\n")
if answer.lower() != "y":
    sys.exit()  # ends application

section_title = "Scenario: Customer Service Center"
print(section_title)
print("-" * len(section_title))

# add clients back to the ArrayList
for i in range(num_records):
    my_array_list.append(clients[i])

# calculates time it would take adding client records to ArrayList
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    # print(my_array_list.search(Client(random_num)))
    print(my_array_list.search_sorted(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print(f"\nIt took {total_time:.6f} seconds to display random records!")


# Scenario 3: Call Center
answer = input("\nContinue (y/n)?\n")
if answer.lower() != "y":
    sys.exit()

section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))

# calculates time it would take adding client records to ArrayList
start_time = time.time()

# add records
current_id = 100001 + num_records + 1
for i in range(1000):
    my_array_list.append(Client(current_id))
    current_id += 1

# display random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    # print(my_array_list.search(Client(random_num)))
    print(my_array_list.search_sorted(Client(random_num)))


for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print(my_array_list.search(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print(f"\nIt took {total_time:.6f} seconds to add, display, and remove records!")

