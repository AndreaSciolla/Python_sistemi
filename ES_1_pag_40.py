def main():
    num = int(input("inserisci un numero:"))
    div = 3
    if num%div == 0:
        print(f"il numero {num}si puo dividere per {div}")
    else:
        print(f"il numero {num}non si puo dividere per {div}")
if __name__ == "__main__":
    main()