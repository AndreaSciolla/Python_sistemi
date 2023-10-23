stringa = "ciao questa e una prova"
stringa_no_voc = [let for let in stringa if (let != 'a' and let !='e' and let !='i' and let !='o' and let !='u')]
print(stringa_no_voc)