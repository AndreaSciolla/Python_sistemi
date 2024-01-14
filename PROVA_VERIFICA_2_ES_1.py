import random
def spostamento():
    return random.choice([1, -1])
def main():
    spostamenti = [spostamento() for _ in range(0, 5*24*60*60)]
    somma = 0
    for i in spostamenti:
        somma += i
    print(f"in una settimana si sposta di {somma} centimetri")
if __name__ == "__main__":
    main()