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

COMMANDS = {helping:"help",
            greeting:"hello",
            add_data:"add",
            change_phone:"change",
            output_phone:"phone",
            show_all:"show all",
            exit:"exit",
            not_command:""
            }

@input_error
def add_data(data):
    name, phone = data
    if not contact_phones.get(name):
        contact_phones[name] = phone

    return f"{name.title()}: {phone}"

@input_error
def change_phone(data):
    name, phone = data
    if contact_phones.get(name):
        contact_phones[name] = phone

    return f"{name.title()}: {phone}"

@input_error
def output_phone(*args):
    for name in contact_phones.keys():
        inf_phone = f"{contact_phones.get(name)}"

    return inf_phone

@input_error
def show_all(*args):
    all_inform = "\n".join([f"{name.title()}: {phone}" for name, phone in contact_phones.items()])
    return all_inform

@input_error
def not_command(*args):
     return "Sorry. Please enter command and other datas"

