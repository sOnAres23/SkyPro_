def strings(words: list) -> list:
    new_list = []
    if words:
        for word in words:
            if word == '' or word[0] == word[-1]:
                new_list.append(word)
    return new_list


print(strings(['', 'madam', 'racecar', 'noon', 'level', '']))
