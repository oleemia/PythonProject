def mask_account_card(info: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    parts = info.split()
    type_name = parts[0]
    number = parts[-1]
    if type_name.lower() == 'счет':
        # Маскируем счет: показываем только последние 4 цифры
        masked_number = '**' + number[-4:]
    else:
        # Маскируем карту: первые 4 и последние 4 цифры, остальное маскируем
        masked_number = number[:4] + ' ' + '**** **** ' + number[-4:]
    return f"{type_name} {masked_number}"

def get_date(date_str: str) -> str:
    """Функция принимает на вход строку с датой в формате
           "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    from datetime import datetime
    dt = datetime.fromisoformat(date_str)
    return dt.strftime('%d.%m.%Y')

print(mask_account_card)
print(get_date)
