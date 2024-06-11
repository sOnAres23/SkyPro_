def strings(words: list) -> list:
    """Функция, которая принимает на вход список со словами
    и возвращает список слов, в которых первая и последняя буквы совпадают"""
    new_list = []
    if words:
        for word in words:
            if word == '' or word[0] == word[-1]:
                new_list.append(word)
    return new_list


if __name__ == "__main__":
    print(strings(['hello', 'dear', 'Vladislav', 'you', 'are', 'talent']))
    print(strings(['', 'madam', 'racecar', 'noon', 'level', '']))
    print(strings([]))