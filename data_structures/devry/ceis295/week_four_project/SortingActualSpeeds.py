# Name: Ben Hill
# Date: 5/23/2023


from MergeSort import MergeSort
from Client import Client
from datetime import date
import time

# display name and date in output
print("Name: ", "Ben Hill")
print("Date: ", date.today())
print()

input_file_name = 'ClientData100.csv'
# input_file_name = 'ClientData1000.csv'
# input_file_name = 'ClientData10000.csv'
# input_file_name = 'ClientData100000.csv'

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

# Scenario: Sorting from a datafile.
section_title = f"Scenario: Sorting {str(num_records)} Records"
print(section_title)
print("-" * len(section_title))

# calculates time it would take to sort records
start_time = time.time()

# call static sort method in the class
MergeSort.sort(clients)

end_time = time.time()
total_time = end_time - start_time
print(f"\nSeconds to sort {num_records} records: {total_time:.6f}")


# Display sorted list
for clt in clients:
    print(clt)
