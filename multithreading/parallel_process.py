##process that run parallel 
##CPU-BOUND tasks-Tasks that are heavy on cpu usage 
import multiprocessing
import time
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Hey this is the square. Square is {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Hey this is the cube. Cube is {i * i * i}")

if __name__== "__main__":
    ## Create the two process 
    p1=multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()
    ##Start the process 
    p1.start()
    p2.start()
    ##Wait the process to complete 
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)