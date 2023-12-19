def welcom():
    print('\nДобро пожаловать в Заметки')


def goodbye():
    print('\nДо новых встреч!')


def menu():
    print("""
    MENU:
    1 - Создать заметку
    2 - Показать заметку
    3 - Показать все заметки
    4 - Показать по дате
    5 - Изменить заметку
    6 - Удалить заметку
    0 - Выйти
    """)


def input_command():
    return input('Введите команду: ')


def input_id():
    return input('Введите ID заметки: ')


def selected_date():
    return input('Введите дату заметки в формате: dd/mm/yyyy: ')


def input_title():
    return input('Введите название заметки: ')


def input_note_text():
    return input('Введите текст из заметки: ')


def output_note(note):
    try:
        print('\n -----------------------',
              f'\nID: {note[0]}\nDATE: {note[1]}\nTITLE: {note[2]}\nNOTE: {note[3]}\n',
              '-----------------------')
    except:
        id_not_found()


def output_all(notes):
    if (notes != []):
        if (len(notes) > 1):
            print(f'\nFound {len(notes)} Notes:')
        else:
            print(f'\nFind {len(notes)} Note:')
        for note in notes:
            print(' -----------------------',
                  f'\nID: {note[0]}\nDATE: {note[1]}\nTITLE: {note[2]}\nNOTE: {note[3]}\n',
                  '-----------------------')
    else:
        print('\nОшибка! Заметок не найдено!',
              '\nСоздайте свою первую заметку')


def output_by_date(notes):
    if (notes != []):
        if (len(notes) > 1):
            print(f'\nFound {len(notes)} Notes:')
        else:
            print(f'\nFind {len(notes)} Note:')
        for note in notes:
            print(' -----------------------',
                  f'\nID: {note[0]}\nDATE: {note[1]}\nTITLE: {note[2]}\nNOTE: {note[3]}\n',
                  '-----------------------')
    else:
        print('\nОшибка! Заметок не найдено!',
              '\nПроверьте правильность даты!')


def created_ok():
    print('\nЗаметка создана успешно!')


def changed_ok():
    print('\nЗаметка отредактирована успешно!')


def deleted_ok():
    print('\nЗаметка удалена успешно!')


def input_error():
    print('\nОшибка ввода! Попробуйте еще раз!')


def id_not_found():
    print('\nОшибка! Заметок не найдено!',
          '\nПроверьте правильность ID')