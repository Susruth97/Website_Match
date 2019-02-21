import threading

def worker(a, b):
    print(a+b)

threads = []
for i in range(5):
    a = 5
    b = 5
    t = threading.Thread(target=worker, args = (a, b))
    threads.append(t)
    t.start()

for t in threads:
    t.join()