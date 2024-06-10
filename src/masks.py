def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер карты пользователя"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return None


def get_mask_account(bank_account: str) -> str | None:
    """Функция маскирующая номер счёта пользователя"""
    if bank_account.isdigit() and len(bank_account) == 20:
        return f"**{bank_account[-4:]}"
    else:
        return None


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
