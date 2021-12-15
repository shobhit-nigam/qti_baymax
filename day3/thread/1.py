import time

def taska():
    for x in range(3, 0, -1):
        print(f"{x} seconds left for A")
        time.sleep(1)

def taskb():
    for x in range(9, 0, -1):
        print(f"{x} seconds left for B")
        time.sleep(1)

taska()
taskb()

for x in range(6, 0, -1):
    print(f"{x} seconds left for main task")
    time.sleep(1)
