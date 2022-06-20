import time

def gera():
    for n in range (50):
        yield n
        time.sleep(0.2)

g = gera()

for v in g:
    print(v)