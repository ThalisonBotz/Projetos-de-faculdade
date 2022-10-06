import threading
from  time import sleep
sem = threading.Semaphore()

def fun1():
    print(" fun1 chegou ")
    sem.acquire()
    for loop in range(1,5):
        print(f" Fun1 trabalhando {loop} ")
        sleep(1)
    sem.release()
    print(" fun1 terminou ")



def fun2():
    print(" fun2 chegou ")
    while not sem.acquire(blocking=False):
        print(" Fun2 sem semaforo disponivel ")
        sleep(1)
    else:
        print("semaforo disponível")
        for loop in range(1, 5):
            print(f" Fun2 trabalhando {loop} ")
            sleep(1)
    sem.release()

t1 = threading.Thread(target = fun1)
t2 = threading.Thread(target = fun2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Todas as threads foram concluidas")