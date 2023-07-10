import re

list_region = {
    "Республика Адыгея": 1,
    "Липецкая область": 48,
    "Республика Башкортостан": "0" + "2",
    "Магаданская область": 49,
    "Республика Бурятия": "0" + "3",
    "Московская область": 50,
    "Республика Алтай": 4,
    "Мурманская область": 51,
    "Республика Дагестан": 5,
    "Нижегородская область": 52,
    "Республика Ингушетия": 6,
    "Новгородская область": 53,
    "Кабардино-Балкарская Республика": 7,
    "Новосибирская область": 54,
    "Республика Калмыкия": 8,
    "Омская область": 55,
    "Республика Карачаево-Черкесия": 9,
    "Оренбургская область": 56,
    "Республика Карелия": 10,
    "Орловская область": 57,
    "Республика Коми": 11,
    "Пензенская область": 58,
    "Республика Марий Эл": 12,
    "Пермский край": 59,
    "Республика Мордовия": 13,
    "Псковская область": 60,
    "Республика Саха (Якутия)": 14,
    "Ростовская область": 61,
    "Республика Северная Осетия - Алания": 15,
    "Рязанская область": 62,
    "Республика Татарстан": 16,
    "Самарская область": 63,
    "Республика Тыва": 17,
    "Саратовская область": 64,
    "Удмуртская Республика": 18,
    "Сахалинская область": 65,
    "Республика Хакасия": 19,
    "Свердловская область": 66,
    "Чувашская Республика": 21,
    "Смоленская область": 67,
    "Алтайский Край": 22,
    "Тамбовская область": 68,
    "Краснодарский край": 23,
    "Тверская область": 69,
    "Красноярский край": 24,
    "Томская область": 70,
    "Приморский край": 25,
    "Тульская область": 71,
    "Ставропольский край": 26,
    "Тюменская область": 72,
    "Хабаровский край": 27,
    "Ульяновская область": 73,
    "Амурская область": 28,
    "Челябинская область": 74,
    "Архангельская область": 29,
    "Забайкальский край": 75,
    "Астраханская область": 30,
    "Ярославская область": 76,
    "Белгородская область": 31,
    "Москва": 77,
    "Брянская область": 32,
    "Санкт-Петербург": 78,
    "Владимирская область": 33,
    "Еврейская автономная область": 79,
    "Волгоградская область": 34,
    "Вологодская область": 35,
    "Воронежская область": 36,
    "Ивановская область": 37,
    "Ненецкий автономный округ": 83,
    "Иркутская область": 38,
    "Калининградская область": 39,
    "Запорожская область": 85,
    "Калужская область": 40,
    "Ханты-Мансийский автономный округ - Югра": 86,
    "Камчатский край": 41,
    "Чукотский автономный округ": 87,
    "Ленинградская область": 47,
    "Ямало-Ненецкий автономный округ": 89,
    "Кемеровская область ": 42,
    "Кемерово": 42,
    "г. Севастополь": 92,
    "Кировская область": 43,
    "Луганская Народная республика": 94,
    "Костромская область": 44,
    "Курганская область": 45,
    "Курская область": 46,
    "Херсонская область": 95,
    "Донецкая Народная республика": 93,
    "Республика Крым": 91
}


def get_region_code(base_string: str) -> int:
    """Функция возвращающая код региона"""
    pattern = base_string
    for key, value in list_region.items():
        if re.findall(pattern, key, re.I):
            return value


