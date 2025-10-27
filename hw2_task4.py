from datetime import datetime; import random; import re;import sys
from pathlib import Path
# Завданя 4
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return 'Contact does not exist.'
        except IndexError:
            return 'Contact does not exist.'
    return inner

@input_error
def command_spliting(user_inp):
    cmd, *args = user_inp.split( )
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def adding_inf(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def get_phonenum(name, contacts):
    phone = contacts.get(name)
    if phone:
        return f"{name}: {phone}"   
    else:
        return f"No contact named {name}"
    
@input_error
def all(contacts):
    all_log=[]
    for i in contacts:
        all_log.append(f'{i}, {contacts.get(i)}')
    return all_log

@input_error
def change(args, contacts):
    if len(args) != 2:
        return "Error: Use 'change <name> <new_phone>'"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}."
    else:
        return f"No contact named {name}."
    
@input_error
def delete(name, contacts):
    contacts.pop(name)
    return 'contact deleted.'


@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_inp = input("Enter a command: ")
        command, args = command_spliting(user_inp) 
        if command == 'hello':
                print('"How can I help you?"')
        elif command in ['close','exit']:
                print("Good bye!")
                break
        elif command == 'add':
                print(adding_inf(args, contacts))
        elif command == 'phone':
                print(get_phonenum(args[0],contacts))
        elif command == 'all':
                for i in all(contacts):
                    print(i)
        elif command == 'change':
                print(change(args, contacts))
        elif command == 'delete':
                print(delete(args[0], contacts))
        else:
                print("Invalid command.")
if __name__ == '__main__':
    main()
