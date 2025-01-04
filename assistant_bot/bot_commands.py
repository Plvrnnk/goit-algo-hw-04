def hello():
    return 'How can I help you?'
    
def add_contact(args, contacts):
    try:
        name, phone = args
        if phone not in contacts.values():
            contacts[name] = phone
            return "Contact added."
        else:
            return 'Phone already exists.'
    except ValueError as v:
        return f'Error: {v}'

def change_contact(args, contacts):
    name, phone = args
    try:
        if name not in contacts.keys():
            return f'Name is not found.'
        contacts[name] = phone
    except ValueError:
        return f'Error: {ValueError}'
    return 'Contact changed'

def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return f"{name}'s phone is {contacts[name]}"
    else:
        return f'Name is not found.'
    
def show_all(contacts):
    return 'Contacts:', contacts

def command_list():
    return 'List of commands:\n1.hello\n2.add (username) (phone)\n3.change (username) (phone)\n4.phone (username)\n5.all\n6.commands\n7.close or exit'