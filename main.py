import multiprocessing

def run_script1():
    import script1

def run_script2():
    import script2

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_script1)
    p2 = multiprocessing.Process(target=run_script2)
    p1.daemon = True  # Set as daemon process
    p2.daemon = True  # Set as daemon process
    p1.start()
    p2.start()
    p1.join()  # No need to join daemon processes
    p2.join()  # No need to join daemon processes
