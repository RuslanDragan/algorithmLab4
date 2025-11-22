import math


# Константа розміру таблиці (для множення беремо 16)
M = 16

# Список вхідних слів (Варіант 11)
WORDS = ["НЕ", "ТОЙ", "БАГАТИЙ", "У", "КОГО", "БАГАТО",
         "ГРОШЕЙ", "А", "ТОЙ", "У", "КОГО", "ДУША", "БАГАТА"]

# Словник позицій
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8,
    'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15,
    'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21, 'С': 22,
    'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29,
    'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def multiplication_hash(key: str) -> int:
    #Хеш-функція методом множення.
    sum_of_positions = 0
    for char in key:
        sum_of_positions += LETTER_POSITIONS.get(char, 0)

    # Константа Кнута A
    A = (math.sqrt(5) - 1) / 2

    # Формула: floor(M * ((sum * A) % 1))
    fractional_part = (sum_of_positions * A) % 1
    return math.floor(M * fractional_part)


def build_open_hash_table(words: list, m: int) -> list:
    #Будує хеш-таблицю з ланцюжками.
    hash_table = [[] for _ in range(m)]

    for word in words:
        address = multiplication_hash(word)
        hash_table[address].append(word)

    return hash_table


def display_hash_table(table: list):
    print(f"\n--- Результат хешування (Ланцюжки, Множення, M={len(table)}) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


# Виконання:
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)