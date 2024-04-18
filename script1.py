import time
from multiprocessing import Pipe

parent_conn, child_conn = Pipe()

def run_script1():
    frame = 0
    while True:
        child_conn.send(frame)
        frame += 1



