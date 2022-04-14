import pika
from flask import Flask, request

import calculator as calc

app = Flask(__name__)

@app.post('/api/prime/<int:number>')
def prime(number):
    result = calc.prime.delay(number)
    return { 'result': result.get() }

@app.post('/api/prime/palindrome/<int:number>')
def prime_palindrome(number):
    result = calc.prime_palindrome.delay(number)
    return { 'result': result.get() }

app.run(debug=True, port=8000, host="0.0.0.0")