contacts = {
    "Brian": {
        "phone": "+255 689 818 494",
        "email": "briankachocho@gmail.com"
    },
    "Bushura": {
        "phone": "+255 744 825 278",
        "email": "isackautowor@gmail.com"
    }
}

def viewContacts(book):
    for name, details in book.items():
        print(f"Jina: {name} | Simu: {details['phone']} | Email: {details['email']}")

viewContacts(contacts)
