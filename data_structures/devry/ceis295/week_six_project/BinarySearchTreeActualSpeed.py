# Ben Hill
# 6/6/2023

from BinarySearchTree import BinarySearchTree
from Client import Client
from datetime import date
import time
import random
import sys


clients = []

input_file = "ClientData.csv"

with open(input_file) as infile:
    for line in infile:
        split_by_comma = line.split(',')
        client_id = int(split_by_comma[0])
        f_name = split_by_comma[1]
        l_name = split_by_comma[2]
        phone = split_by_comma[3]
        email = split_by_comma[4]
        create_clt_obj = Client(client_id, f_name, l_name, phone, email)
        clients.append(create_clt_obj)

num_records = len(clients)

# create BST to test real-world speeds
my_bst = BinarySearchTree()

# SCENARIO FUNCTIONS
def print_name():
    print("\nName: Ben Hill")
    print(f"Date: {date.today()}\n")


def next_scenario():
    answer = input("Continue (y/n)? \n\n")
    if answer.lower() != "y":
        sys.exit()


# Scenario 1: Printer, Call, Service Queue
def printer_call_service():
    print_name()
    section_title = "Scenario: Printer, Call, Service Queue"
    print(section_title)
    print("-" * len(section_title))


    # time to insert records
    start_time = time.time()
    for i in range(num_records):
        my_bst.insert(clients[i])

    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nSeconds to add records: {total_time:.6f}\n")

    # how long does it take to remove (smallest) from BST
    start_time = time.time()
    for i in range(num_records):
        my_bst.remove_minimum()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Seconds to remove records: {total_time:.6f}\n")


# Scenario 2: Customer Service Center
def cust_serv_center():

    # ADD clients to BST
    for i in range(num_records):
        my_bst.insert(clients[i])

    # how long does it take to randomly display 1000 client records to BST
    start_time = time.time()
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + num_records
        random_num = random.randint(smallest_id, largest_id)
        print(my_bst.search(Client(random_num)))

    end_time = time.time()
    total_time = end_time - start_time

    print_name()
    section_title = "Scenario: Customer Service Center"
    print(section_title)
    print("-" * len(section_title))

    print(f"\nSeconds to display 1000 random records for Customer Service Center records: {total_time:.6f}\n")


def call_center():
    # ADD clients to BST
    for i in range(num_records):
        my_bst.insert(clients[i])

    # how long does it take to add more client records to BST,
    # randomly display 1000 records, randomly remove 1000 records from BST
    start_time = time.time()

    # add records
    current_id = 100001 + num_records + 1
    for i in range(1000):
        my_bst.insert(Client(current_id))
        current_id += 1

    # display records
    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + num_records
        random_num = random.randint(smallest_id, largest_id)
        print(my_bst.remove(Client(random_num)))

    for i in range(1000):
        smallest_id = 100001
        largest_id = smallest_id + num_records
        random_num = random.randint(smallest_id, largest_id)
        print(my_bst.search(Client(random_num)))

    end_time = time.time()
    total_time = end_time - start_time

    print_name()
    section_title = "Scenario: Call Center"
    print(section_title)
    print("-" * len(section_title))

    print("\nSeconds to add records,")
    print(" display 1000 random records,")
    print(f" and remove 1000 records for Call Center records: {total_time:.6f}\n")



# SCENARIO ONE
printer_call_service()
next_scenario()

# SCENARIO TWO
cust_serv_center()
next_scenario()

# SCENARIO THREE
call_center()
