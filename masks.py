def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры,
    с разделением на блоки по 4 символа и звездочками вместо скрытых цифр"""
    # Заменяем средние символы звездочками
    masked_part = "*" * (len(card_number) - 6 - 4)
    # Формируем маскированный номер
    masked_number = f"{card_number[:6]}{masked_part}{card_number[-4:]}"
    # Разбиваем на блоки по 4 символа
    parts = []
    for i in range(0, len(masked_number), 4):
        parts.append(masked_number[i : i + 4])
    return " ".join(parts)

def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми первые 2 и последние 2 символа,
    остальные заменяет звездочками"""
    if len(account_number) <= 4:
        # Если длина короткая, маскируем все кроме первых двух
        return account_number[0:2] + "*" * (len(account_number) - 2)
    else:
        masked_part = "*" * (len(account_number) - 4)
        return account_number[:2] + masked_part + account_number[-2:]

# Пример работы функции
input_card_number = "7000792289606361"
masked_output = get_mask_card_number(input_card_number)
# Печать результата
print(f"Исходный номер карты: {input_card_number}")
print(f"Маскированный номер карты: {masked_output}")