num = int(input("inserisci un numero: "))
lista = [2**i for i in range (num) if (2**i < num)]
print(lista)