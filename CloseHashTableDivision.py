
# Константа розміру таблиці (за завданням M=13)
M = 13

# Список вхідних слів (Варіант 11)
WORDS = ["НЕ", "ТОЙ", "БАГАТИЙ", "У", "КОГО", "БАГАТО",
         "ГРОШЕЙ", "А", "ТОЙ", "У", "КОГО", "ДУША", "БАГАТА"]

# Словник позицій (Український алфавіт)
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8,
    'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15,
    'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21, 'С': 22,
    'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29,
    'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def primary_hash(key: str) -> int:
    #h(k) = (сума позицій букв) mod M. Первинна хеш-функція.
    sum_of_positions = 0
    for char in key:
        sum_of_positions += LETTER_POSITIONS.get(char, 0)
    return sum_of_positions % M


def build_closed_hash_table(words: list, m: int) -> list:
    # 1. Ініціалізація таблиці: M порожніх слотів
    hash_table = [None] * m

    for word in words:
        # Крок 2а: Обчислення початкової адреси
        start_address = primary_hash(word)
        address = start_address

        # Крок 2б: Лінійне дослідження (Linear Probing)
        inserted = False
        for i in range(m):
            # h(k,i) = (h(k) + i) mod M
            address = (start_address + i) % m

            # Перевірка, чи комірка вільна
            if hash_table[address] is None:
                # Вставлення ключа
                hash_table[address] = word
                inserted = True
                break

        if not inserted:
            print(f"Помилка: Таблиця заповнена. Не вдалося додати слово: {word}")

    return hash_table


def display_hash_table(table: list):
    print(f"\n--- Хеш-таблиця (Відкрита адресація, Ділення, M={len(table)}) ---")
    print("Індекс | Слово")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")


# Виконання:
hash_table = build_closed_hash_table(WORDS, M)
display_hash_table(hash_table)