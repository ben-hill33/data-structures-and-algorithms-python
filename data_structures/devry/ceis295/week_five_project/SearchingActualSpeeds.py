# Ben Hill
# 5/29/2023


from LinearSearch import LinearSearch
from BinarySearch import BinarySearch
from Quicksort import Quicksort
from Client import Client

from datetime import date
import random
import time
import sys


print("Name:", "Ben Hill")
print("Date:", date.today())
print()


# input_file_name = 'ClientData100.csv'
# input_file_name = 'ClientData1000.csv'
# input_file_name = 'ClientData10000.csv'
input_file_name = 'ClientData100000.csv'

clients = []

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

# how many client objects do we have?
num_records = len(clients)

# Scenario: Search for 1000 records from a datafile.
section_title = f"Scenario: Searching Through {str(num_records)} Records"
print(section_title)
print("-" * len(section_title))

Quicksort.sort(clients)
start_record = 100001
end_record = start_record + num_records

# calculates time it would take to search records
start_time = time.time()

# How long does it take to do a random linear search through the records
for i in range(1000):
    client_id = random.randint(start_record, end_record)
    client_obj = Client(client_id)
    result = BinarySearch.search(clients, client_obj)

    if result is None:
        print(client_obj, "was not found.")
    else:
        print(result)

end_time = time.time()
total_time = end_time - start_time
print(f"\nSeconds to search for 1000 {num_records} records: {total_time:.6f}\n")
