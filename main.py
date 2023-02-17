nombres = int(input("Entrez la quantité de nombres à afficher : "))

def fibonacci_recursive(n):
   if n <= 1:
       return n
   else:
       return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)

print("Les {} premiers nombres de la suite de Fibonacci sont :".format(nombres), end=" ")

for i in range(nombres):
    print(fibonacci_recursive(i), end=" ")