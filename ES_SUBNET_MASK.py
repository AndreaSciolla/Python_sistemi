num = int(input("inserisci un numero intero(1..31)"))
sub_dec = "1"*num + "0"*(32 - num)

group1 = sub_dec[0:8]
group2 = sub_dec[8:16]
group3 = sub_dec[16:24]
group4 = sub_dec[24:32]

group1 = int(group1, 2)
group2 = int(group2, 2)
group3 = int(group3, 2)
group4 = int(group4, 2)
print(sub_dec)
ip = f"{group1}.{group2}.{group3}.{group4}"
print(ip)



