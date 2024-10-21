import random
def generate_password(n):
    result = ""
    used_pairs = set()
    for i in range(1, n):
        for j in range(i+1, n):
            if (i + j) <= n and n % (i + j) == 0:
                if (i, j) not in used_pairs and (j, i) not in used_pairs:
                    result += str(i) + str(j)
                    used_pairs.add((i, j))

    return result
n = random.randint(3, 20)
password = generate_password(n)
print(f"Число из первой вставки: {n}")
print(f"Нужный пароль: {password}")