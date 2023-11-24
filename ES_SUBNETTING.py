def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return ("0"*(8-l) + b)

ipAddress = input("inserisci un indirizzo IPv4: ")
groups = ipAddress.split(".") #lista che contiene i gruppi; la split ritorna una lista di stringhe
groups = [int(group) for group in groups] #convertire i gruppi da stringhe a interi
groups_b = [bin(elemento) for elemento in groups]
print(groups_b)
#print(completa8bit(groups_b[3]))
groups_strbin = [completa8bit(strbin) for strbin in groups_b]
print(groups_strbin)
print(".".join(groups_strbin))