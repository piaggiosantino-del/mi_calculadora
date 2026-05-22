# main.py
from calculadora import sumar, restar, multiplicar, dividir

print("=" * 40)
print("   CALCULADORA SIMPLE")
print("=" * 40)

a = 10
b = 5

print(f"\nSuma: {a} + {b} = {sumar(a, b)}")
print(f"Resta: {a} - {b} = {restar(a, b)}")
print(f"Multiplicación: {a} * {b} = {multiplicar(a, b)}")
print(f"División: {a} / {b} = {dividir(a, b)}")

print("\n" + "=" * 40)
