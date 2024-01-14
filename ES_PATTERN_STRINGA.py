import sys

def getStringa():
    s = ""
    while True:
        c = sys.stdin.read(1)
        if c == '*':
            break
        if c == '\t':
            s += '\n'
        else:
            s += c
    return s + "\0" 

def getPattern():
    s = ""
    while True:
        c = sys.stdin.read(1)
        if c == '\n':
            break
        else:
            s += c
    return s + "\0"

def main():

    s = getStringa()
    #pat = getStringa()
    print(s)
    #print(pat)


if __name__ == "__main__":
    main()