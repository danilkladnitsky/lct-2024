import random


def random_hex_color():
    # Генерируем случайные значения для каждого из компонентов RGB
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = '0x{:02x}{:02x}{:02x}'.format(r, g, b)
    print('color', color)
    # Форматируем значение как HEX-строку
    return color

colors_dict = {
    'black': '0x000000',
    'white': '0xffffff',
    'red': '0xff0000',
    'lime': '0x00ff00',
    'blue': '0x0000ff',
    'yellow': '0xffff00',
    'cyan': '0x00ffff',
    'magenta': '0xff00ff',
    'silver': '0xc0c0c0',
    'gray': '0x808080',
    'maroon': '0x800000',
    'olive': '0x808000',
    'green': '0x008000',
    'purple': '0x800080',
    'teal': '0x008080',
    'navy': '0x000080',
    'orange': '0xffa500',
    'aliceblue': '0xf0f8ff',
    'antiquewhite': '0xfaebd7',
    'aqua': '0x00ffff',
    'aquamarine': '0x7fffd4',
    'azure': '0xf0ffff',
    'beige': '0xf5f5dc',
    'bisque': '0xffe4c4',
    'blanchedalmond': '0xffebcd',
    'blueviolet': '0x8a2be2',
    'brown': '0xa52a2a',
    'burlywood': '0xdeb887',
    'cadetblue': '0x5f9ea0',
    'chartreuse': '0x7fff00',
    'chocolate': '0xd2691e',
    'coral': '0xff7f50',
    'cornflowerblue': '0x6495ed',

    'junior': '0x009099',
    'shool': '0xffffff',
    'meet_squre':'0xffc5a6',

    'football': '0x97ca47',
    'basketball': '0x006e37',
    'volleyball': '0xffa1a9',
    'race': '0x00b79f',

    'main_zone': '0x37d8cf',
    'sport_zone': '0xff385c',
    'relax_zone': '0xe3ebd4',
    'ground_zone': '0xccd4bf',

}


# Пример использования
# print(random_hex_color())