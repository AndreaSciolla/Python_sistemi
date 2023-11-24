def cercaPerNome(nome, rubrica):
    for num in rubrica:
        if nome == rubrica[num]:
            return(num)
    return None  #se non trova il nome restituisce none

def cercaPerNumero(num, rubrica):
        if num in rubrica:
            return(rubrica[num])
        else:
            return None

def main():

    rubrica = {}
    numeri = "0123456789"
    f = open("rubrica.txt", "r")
    for riga in f.readlines():
        campi = riga.split(", ")
        rubrica[int(campi[1].replace("\n", ""))] = campi[0]
    f.close()

    nomenum = input("inserisci il nome o numero da cercare: ")
    if nomenum[0] in numeri:
        print(cercaPerNumero(nomenum, rubrica))
    else:
        print(cercaPerNome(nomenum, rubrica))
        
if __name__ == "__main__":
    main()