import threading
from random import randint
import time


class Bank:

    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = threading.Lock()



    def deposit(self):
        for i in range(100):
            rand = randint(50, 501)
            self.balance = self.balance + rand
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand = randint(50, 501)
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance = self.balance - rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')






