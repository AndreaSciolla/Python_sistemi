def main():
    x = float(input("inserisci il primo numero:"))
    y = float(input("inserisci il secondo numero:"))
    if x>y:
        y, x = x, y
    print(f"{y}, {x}")
if __name__ == "__main__":
    main()