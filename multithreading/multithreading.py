##Multithreading 
 ##When to Use Multithreading
# Understanding when to use multithreading is crucial. There are two main reasons:

# I/O Bound Tasks: Tasks that spend more time waiting for I/O operations, such as file operations or network requests.
# Concurrent Execution: When you want to improve the throughput of your application by performing multiple operations concurrently.


import threading
import time 

def print_numbes():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")


def print_letters():
    for letter in "ABCD":
        time.sleep(2)
        print(f"Letter: {letter}")
##cretaing 2 threads 
t1 = threading.Thread(target = print_numbes)
t2 = threading.Thread(target= print_letters)
t = time.time()
t1.start()
t2.start()
##Wait for thread to complete 
t1.join()
t2.join()
# print_numbes()
# print_letters()
finished_time =time.time()-t
print(f"Time taken: {finished_time} seconds")