'''
Real-world example: MultiProcessing for CPU-bound Tasks 
Scenario: Factorial Calculation 
involves significant computations,espically for large numbers 
involves significantly computational work.Multiprocssing can be used to distribute the workload across multiple CPU cores,improve Performance 
'''
import multiprocessing
import math
import sys
import time
#increase the maximum numbers of digit for integer conversion 
sys.set_int_max_str_digits(100000)
##Function to compute factorial of a given number 
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == '__main__':
    # Define a list of large numbers for factorial calculation
    numbers = [6000, 7000, 8000]
    # Start the timer to measure execution time
    start_time = time.time()
    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        # Map the compute_factorial function to the list of numbers
        results = pool.map(compute_factorial, numbers)
        # End the timer
    end_time = time.time()

    # Print the results and the time taken
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")