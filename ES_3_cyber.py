def count_calls_f(x):
    # Usiamo una variabile globale per contare le chiamate
    global call_count
    call_count += 1

    if x <= 0:
        return x
    else:
        return count_calls_f(x-1) - count_calls_f(x-2)

# Inizializziamo la variabile globale per il conteggio delle chiamate
call_count = 0

# Calcoliamo f(20) e contiamo le chiamate
result = count_calls_f(20)

# Stampa il risultato e il numero di chiamate
print(f"Risultato di f(20): {result}")
print(f"Numero totale di chiamate per f(20): {call_count}")
