import ipaddress

ipv4 = input("inserisci indirizzo ipv4: ")
subnet =  input("inserisci la subnetmask: ")
ipv4pieno = ipv4 + subnet
ip = ipaddress.IPv4Address(ipv4)
if ip.is_private:
    print("è privato")
if ip.is_loopback:
    print("è loopback")
if ip == ipaddress.IPv4Network(ipv4pieno, strict=False):
    print("è di rete")
else:
    print("non è di rete")