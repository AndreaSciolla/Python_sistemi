def main1():

    parola = "sporgis"
    for k in range(0, len(parola)):
        if k % 2 != 0:
            print({parola[k]})

def main():
     parola = "sporgis"
     print(parola[1::2]) #parte dall'1 e ogni volta salta di 2

if __name__ == "__main__":
    main()