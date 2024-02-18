#spiegazione del DIZIONARIO in python
#il DIZIONARIO è una condizione di coppie -> chiave:valore
#non ha indici, ma si indicizza per chiave quindi la chiave deve essere univoca
#la chiave deve essere di un solo tipo;

dizionario = {"nome": "Mario", "cognome": "Rossi"}     #per il  dizionario i limitatori sono le graffe
#uguale a: lista=["Mario", "Rossi"]

print(dizionario["nome"]) #stampa il valore con chiave nome

#aggiungere un elemento al dizionario
dizionario["data di nascita"] = "01/01/1900" 
dizionario["anni"] = 123

#sovrascrivere l'elemento con chiave nome
dizionario["nome"] = "Luca" 

print(dizionario)

# se si vuole ciclare sia su chiave che su collegamenti si usa .itens()
'''esempio:
    for chiave, valori in diz.items():
'''

#cilcare su un dizionario

for chiave in dizionario:  #x cicla sulle chiavi
    print(f"Chiave: {chiave} - Valore: {dizionario[chiave]}")


#esempio dizionario:

rubrica = {383883820: "Mario Rossi", 23749245: "Alice Verdi", 2345675567: "Luca Giallo"}