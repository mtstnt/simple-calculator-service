import os
from celery import *

app = Celery('calculator', broker=f'amqp://guest:guest@rabbitmq:5672', backend=f'redis://redis:6379')

def check_prime(n: int) -> bool:
    co = 0
    for i in range(1, n + 1):
        if n % i == 0:
            co += 1

    return True if co == 2 else False

def check_palindrome(n: int) -> bool:
    return True if int(str(n)[::-1]) == n else False

@app.task
def prime(n: int):
    number = 2
    while True:
        if check_prime(number):
            n -= 1
        if n <= 0:
            break
        number += 1
    return number
        
@app.task
def prime_palindrome(n: int) -> bool:
    number = 2
    while True:
        if check_prime(number) and check_palindrome(number):
            n -= 1
        if n <= 0:
            break
        number += 1
    return number