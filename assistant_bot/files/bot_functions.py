def hello():
    print('How can I help you?')
    
def add_contact(args, contacts):
    with open('info.txt', 'a+') as fl:
        name, phone = args
        try:
            if phone in contacts.values():
                return 'Phone already exists.'
            contacts[name] = phone
            fl.write(str(contacts).replace('{','').replace('}','') + '\n')
        except ValueError as v:
            print(f'Error: {v}')
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    try:
        if name in contacts.keys():
            return f'Name is not found: {ValueError}'
        contacts[name] = phone
        with open('info.txt', 'w') as fl:
            fl.write(str(contacts).replace('{','').replace('}','') + '\n') 
            
    except ValueError as v:
        print(f'Error: {v}')
    return 'Contact changed'

def show_phone(args, contacts):
    name = args[0]
    try:
        with open('info.txt', 'r') as fl:
            contacts = {}
            for line in fl:
                line = line.strip().replace("'", "").replace(":", "")
                if line:
                    parts = line.split()
                    if len(parts) == 2:
                        contact_name, phone = parts
                        contacts[contact_name] = phone
            if name in contacts:
                return contacts[name]
        return f"Error: Contact '{name}' not found."
    except ValueError as v:
        print(f'Error: {v}')
        

def show_all(contacts):
    with open('info.txt', 'r') as fl:
        lines = fl.readlines()
        for line in lines:
            print(line)
    
def command_list():
    print('List of commands:\n1.hello\n2.add (username) (phone)\n3.change (username) (phone)\n4.phone (username)\n5.all\n6.commands\n7.close or exit')