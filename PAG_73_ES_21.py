stringa = "ciaoquestaeunaprova"
stringa_no_voc = [let for let in stringa if (let != 'a' and let !='e' and let !='i' and let !='o' and let !='u')]
print("".join(stringa_no_voc)) #join attacca una lista di stringhe usando come carattere separatore quello tra ""