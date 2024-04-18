import time
from script1 import parent_conn

while True:
    frame = parent_conn.recv()
    print(frame)
