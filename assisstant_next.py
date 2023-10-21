def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Oops, something's wrong with the name or phone number."
        except KeyError:
            return "Hmm, can't find that contact."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact does not exist."
    else:
        contacts[name] = phone
        return "Contact updated."


@input_error
def get_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return "Contact does not exist."
    else:
        return contacts[name]


def get_all_contacts(contacts):
    print("List of contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Oops, I need a name and a phone number.")
            else:
                print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Oops, I need a name and a phone number.")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Oops, I need a name.")
            else:
                print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()