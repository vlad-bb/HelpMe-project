def greeting(*args):  # вітання
    return 'Hello! Can I help you?'


def exiting(*args):  # вихід
    return 'Good bye!'


def helping(*args):  # меню с описом функцій, при додаванні функції - пишіть сюди команду для запуску та опис функції
    return """Command format:
    help or ? -> this help;
    hello -> greeting;
    good bye or close or exit or . -> exit the program"""


def unknown_command(*args):  # заглушка для невідомих команд
    return 'Unknown command! Try again!'


# список команд - при додаванні команди - прописуйте сюди.
COMMANDS = {greeting: ['hello'],
            helping: ['?', 'help'],
            exiting: ['good bye', 'close', 'exit', '.']
            }


# парсер вводу
def command_parser(user_command: str) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


# main функція проекту
def main():
    print(f'Menu:''\n'
          f'1. AddressBook''\n'
          f'2. NoteBook''\n'
          f'3. CleanFolder')
    while True:
        user_command = input('>>> ')
        command, data = command_parser(user_command)
        print(command(*data))
        if command is exiting:
            break


if __name__ == '__main__':
    main()
