# Name: Ben Hill
# Date: 9/18/2022

from Queue import Queue
from Call import Call
from datetime import date
import time
import random

print("Name:", "Ben Hill")
print("Date:", date.today())
print()

calls = []

input_file_name = "../data/CallData.csv"
with open(input_file_name) as in_file:
    for line in in_file:
        split_at = line.split(',')
        client_id = int( split_at[0] )
        client_name = split_at[1]
        client_phone = split_at[2]
        # Create Call object based on data from the line
        a_call = Call(client_id, client_name, client_phone)
        calls.append(a_call)


# Queue object for calls
calls_waiting = Queue()
call_num = 0

seconds = int( input("How many seconds do you want to simulate? ") )

# run sim for the given number of seconds
for i in range(seconds):
    print("-" * 40)
    time.sleep(2) # pause app for given number of seconds
    random_event = random.randint(1, 3)
    # do event based on random number generated
    if random_event == 1:
        print("Call received, caller added to queue.")
        calls_waiting.enqueue( calls[call_num] )
        call_num += 1 # sets up next call sim
        print(f"\tNumber of calls waiting in queue: {calls_waiting.get_length()}")
    elif random_event == 2:
        print("Call sent to representative for service.")
        if calls_waiting.get_length() > 0:
            print("Caller information:")
            print(calls_waiting.dequeue())
        else:
            print("The call waiting queue is empty.")
        print(f"\tNumber of calls waiting in queue: {calls_waiting.get_length()}")
    else:
        print("Nothing to show at this time.")
        print(f"\tNumber of calls waiting in queue: {calls_waiting.get_length()}")

print("\n 'Automatic Call Distributor' simulation has concluded.")
