from http import HTTPStatus
import pika
from flask import Flask, Response, request

import calculator as calc

app = Flask(__name__)

@app.get('/api/prime/<int:number>')
def prime(number):
    result = calc.prime.delay(number)
    return { 'result': result.get() }

@app.get('/api/prime/palindrome/<int:number>')
def prime_palindrome(number):
    result = calc.prime_palindrome.delay(number)
    return { 'result': result.get() }

app.run(debug=True, port=8000, host="0.0.0.0")