def mask_account_card(client_information: str) -> str:
    """Функция, которая возвращает с замаскированным номером карты или счета"""

    if "Счет" in client_information:
        return client_information[:-20] + f"**{client_information[-4:]}"
    else:
        name = client_information[-16:]
        new_name = f"{name[:4]} {name[4:6]}** **** {name[12:]}"
        new_card = client_information[:-16] + new_name
        return new_card


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("MasterCard 7158300734726758"))


def get_data(date: str) -> str:
    """Функция для преобразования даты"""
    new_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return new_date


print(get_data("2018-07-11T02:26:18.671407"))
