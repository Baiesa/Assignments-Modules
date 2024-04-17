

contacts = []


def add_contact(name, phone, email):
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)


def remove_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)


def display_contact():
    for contact in contacts:
        print(f"name: {contact["name"]},phone: {contact["phone"]}, email: {contact["email"]} ")
