TIPO_POSS = ["umanoide", "normale"]
class Robot():
    def __init__(self, nome, peso, tipo):
        self.nome = nome
        if peso > 0:
            self.peso = peso
        else:
            self.peso = 1
        self.tipo = "normale"
        for tipi in TIPO_POSS:
            if tipo == tipi:
                self.tipo = tipo

    def stampaNome(self):
        print(f"il nome del robot è : {self.nome}")

    def isPericoloso(self):
        return (self.tipo == "umanoide" and self.peso > 100)
            


def main():
    nome = input("inserisci il nome del robot: ")
    peso = int(input("inserisci il peso del robot: "))
    tipo = input("inserisci il tipo del robot[umanoide o normale]: ")
    rob = Robot(nome, peso, tipo)

    if  rob.isPericoloso():
        print("pericolo")
    else:
        print("no pericolo")


if __name__ == "__main__":
    main()