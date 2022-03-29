import time

timer = 0
startTime = int(time.time())

def timer(self):
    global timer
    global startTime
    sessionTime = int(time.time()) - startTime
    print(sessionTime)
    