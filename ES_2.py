def main():

    a = float(input("inserisci un numero: "))
    print(f"il tipo di a è{type(a)}")
    if a > 5:
        print("a è maggiore di 5")
    elif(a<=5) and (a>=0):
        print("a è >= 0 e <= 5")
    else:
        print("a e minore o uguale a 0")
if __name__ == "__main__":
    main()