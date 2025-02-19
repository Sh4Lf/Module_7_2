def custom_write(file_name, strings):
    strings_positions = {}

    try:
        with open(file_name, 'wb') as f:
            for index, string in enumerate(strings):
                byte_position = f.tell()
                f.write(string.encode('utf-8') + b'\n')
                strings_positions[(index + 1, byte_position)] = string

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return strings_positions


info = [
    'Текст для записи.',
    'Используйте кодировку utf-8.',
    'Потому что есть 2 языка!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)