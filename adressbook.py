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


def input_error(my_func):
    def wrapper(*args):
        try:
            return my_func(*args)
        except IndexError:
            return "(Index) Enter the command correctly or enter command (help)"

        except ValueError:
            return "(Value) Enter the name and phone correctly or enter command (help)"

        except KeyError:
            return "(Key) Enter the name correctly or enter command (help)"

        except TypeError:
            return "Incorrect data entry. Enter the command, name and other correctly or enter command (help)"

    return wrapper


contact_phones = {}


@input_error
def add_data(*args):
    name, phone = args[0], args[1]
    if contact_phones:
        for k, v in contact_phones.items():
            if k == name:
                if phone in v:
                    return f'This number already has in contact{k.title()}'
                else:
                    v.append(phone)
                    return f'Number {phone} add to Contact {name.title()} successful'
            else:
                contact_phones[name] = [phone]
                return f'Contact {name.title()}: {phone} add successful'
    else:
        contact_phones[name] = [phone]
        return f'Contact {name.title()}: {phone} add successful'


@input_error
def change_phone(data):
    name, phone = data
    if contact_phones.get(name):
        contact_phones[name] = phone

    return f"{name.title()}: {phone}"


@input_error
def output_phone(*args):
    for name in contact_phones.keys():
        return f"{contact_phones.get(name)}"


@input_error
def show_all(*args):
    if contact_phones:
        return "\n".join([f"{name.title()}: {phones}" for name, phones in contact_phones.items()])
    else:
        return f'AddressBook is empty'


# список команд - при додаванні команди - прописуйте сюди.
COMMANDS = {greeting: ['hello'],
            helping: ['?', 'help'],
            exiting: ['good bye', 'close', 'exit', '.'],
            add_data: ['add'],
            change_phone: ["change"],
            output_phone: ["phone"],
            show_all: ["show all"]
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


def main():
    while True:
        user_command = input('Enter command:>>> ')
        if user_command == 'exit':
            return f'Exit'
        command, data = command_parser(user_command)
        print(command(*data))
        if command is exiting:
            break
