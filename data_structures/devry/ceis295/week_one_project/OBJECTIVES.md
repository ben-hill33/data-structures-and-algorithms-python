# Module 1: ArrayList Real-World Speeds

## Objectives

- To add Client data type to the ArrayList
- To develop Python code that tests the ArrayList's real world speeds
- To develop an Excel table that displays relevant real-world speeds

We are discussing the algorithm speeds using theoretical nomenclature, including Big-O notation. At the same time, it is important to test the algorithm speeds using real-world data.  Does the algorithm perform as expected?  Write code to test the algorithm and find out!

You can test the speed of a process by checking the current time.  Then, run the process.  Finally, check the current time again.  Subtract the current time at the start of the process from the current time at the end of the process.  The different in time will be the time that the process took to complete.

For example, how long does it take to say “Hello Everyone!” a total of 1000 times?  Run this code in your Python IDE:

```py
#Name: Ben Hill
#Date: Sep 7, 2022
import time    # use time library to time the code executions

# get current time before the process
start_time = time.time()

# run the process
for i in range(1000):
    print( "Hello Everyone!" )

# get current time after the process
end_time = time.time()

# subtract start time from end time to get time used by process
total_time = end_time - start_time

# Show the result.  Note: .6f means “show six decimal places”
print("\nSeconds run 1000 times: {:.6f}".format(total_time))
```

## Steps

1. Create a new folder in your CEIS295 folder called “Week 1 Project”. Create an Excel table in this folder so we can record the time that it takes to perform real-world processes based on common scenarios. We are going to compare the ArrayList data structure that we created this week with data structures that we are going to create over the next few weeks. In addition, we are going to compare the ArrayList search feature when you use unsorted data versus when you use sorted data. The Excel table should look something like this:

2. In this same folder, create a file called `TimeProcess.py` and place the code listed above in the file. Run the code and check to see how long it takes your computer to say “Hello Everyone!” one thousand times. Make sure you understand how to check the time of a process based on this technique. Also, make sure your name and the current date are listed at the top of the code.

3.	Download the `ClientData.csv` file and place the file in your “Week 1 Project” folder. Open the file and look at the data. We will read the data in this file so we can work with a real-world sized dataset to test our algorithms. This dataset is considered “small” based on real-world data, but the dataset will give us a way to test our algorithm speed.

4.	Download the `Quicksort.py` file and place it in your “Week 1 Project” folder. We are going to use this code to sort our data and check the speed difference when you use sorted versus unsorted data with an ArrayList.

5.	In this same folder, create a Client class based on the following UML diagram. The `__eq__` method means “equals” and it should return `True` if this object is the same as the other object, which is received in the parameter. Otherwise, it should return False. The `__str__` method means “string” and should return the `__cliend_id`, `__first_name`, and `__last_name` in this format:  1000, Black, Jack
Also, make sure your name and the current date are listed at the top of the code.
