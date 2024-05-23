import pickle
from operations.commands import AddressBook

def save_data(book, filename="addressbook.pkl"):
    try:
        with open(filename, "wb") as f:
            pickle.dump(book, f)
    except FileNotFoundError:
        return AddressBook()


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
