from adressbook import main as amain

# main функція проекту
def main():
    while True:
        print('Menu:',
              '1. AddressBook',
              '2. NoteBook',
              '3. CleanFolder',
              '4. Close program', sep='\n')
        user_command = input('Press menu button: >>> ')
        if user_command == '1':
            print(f'AddressBook Manager: info -> write "help" or "?"')
            result = amain()
            if result == 'Exit':
                continue
        elif user_command == '4':
            print('Good bye!')
            break


if __name__ == '__main__':
    main()
