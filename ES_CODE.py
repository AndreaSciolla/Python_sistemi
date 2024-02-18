class Coda:
    def __init__(self):
        self.lista = []
    def is_empty(self):
        return len(self.lista) == 0
    def enqueue(self, x):
        self.lista.append(x)
    def dequeue(self):
        if self.is_empty():
            print("lista vuota")
            return None
        else:
            return self.lista.pop(0)
    def stampa(self):
        print(self.lista)
    
def main():
    coda = Coda()
    print(coda.dequeue())
    coda.enqueue(10)
    coda.enqueue(9)
    coda.enqueue(8)
    coda.stampa()
    print(coda.dequeue())
    coda.stampa()
if __name__ == "__main__":
    main()