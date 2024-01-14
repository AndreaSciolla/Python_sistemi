def is_gabibboso(number):
    str_number = str(number)

    if int(str_number[0]) % 2 != 0:
        return False

    for i in range(1, len(str_number)):
        if int(str_number[i]) <= int(str_number[i - 1]):
            return False

    return True

def count_gabibbosi_numbers(max_value):
    count = 0

    for num in range(10, max_value + 1):
        if is_gabibboso(num):
            count += 1

    return count

max_value = 9999
total_gabibbosi_numbers = count_gabibbosi_numbers(max_value)
print(f"Il numero totale di numeri Gabibbosi fino a {max_value} è: {total_gabibbosi_numbers}")
