import math
def main():
    lista = [i**2 for i in range(0, int(math.sqrt(200))) if(i*i % 2 != 0)]
    #lista = [i**2 for i in range(0, int(math.sqrt(200))) if(i*i % 2 != 0)]
    print(lista)
if __name__ == "__main__":
        main()