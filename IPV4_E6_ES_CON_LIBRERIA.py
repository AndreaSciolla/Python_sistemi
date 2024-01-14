import ipaddress

ipv4 = input("inserisci indirizzo ipv4: ")
subnet =  input("inserisci la subnetmask (/n): ")
ipv4pieno = ipv4 + subnet
ip = ipaddress.IPv4Address(ipv4)
if ip.is_private:
    print("è privato")
if ip.is_loopback:
    print("è loopback")
iprete = ipaddress.IPv4Network(ipv4pieno, strict=False)
if ipv4pieno == str(iprete):
    print(f"è di rete perchè l'indirizzo {ipv4pieno} coincide con {iprete}")
else:
    print(f"non è di rete perchè l'indirizzo {ipv4pieno} non coincide con {iprete}")
print(f"indirizzo di rete: {iprete}")
hosts = list(iprete.hosts())
print(f"il primo ip utilizzabile è: {hosts[0]}")
print(f"l'ultimo ip utilizzabile è: {hosts[-1]}")
