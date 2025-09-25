#Modul 6 Home work 1

from collections import UserDict #Cловник для зберігання записів.

class Field: #Клас для полів.Зберігає значення у self.value.
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field): #Перевіряє, що ім’я не порожнє.
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)

class Phone(Field): #Перевіряє формат номера.
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must be 10 digits.")
        super().__init__(value)

class Record: #Зберігає ім’я (Name) та список телефонів (Phone).
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number): #Додає телефон.
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number): #Видаляє телефон.
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone not found.")

    def edit_phone(self, old_number, new_number): #Змінює існуючий телефон.
        phone = self.find_phone(old_number)
        if phone:
            phone.value = Phone(new_number).value
        else:
            raise ValueError("Old phone not found.")

    def find_phone(self, phone_number): #Шукає телефон.
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self): #Формат виводу.
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict): #Робимо словник.
    def add_record(self, record): #Додає Record у словник.
        self.data[record.name.value] = record

    def find(self, name): #Повертає запис по імені.
        return self.data.get(name)

    def delete(self, name): #Видаляє запис.
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found.")

    def __str__(self): #Виводимо всю адресну книгу.
        return '\n'.join(str(record) for record in self.data.values())

#Перевірка.
if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("All contacts:")
    print(book)

    john = book.find("John") #Редагування телефону.
    john.edit_phone("1234567890", "1112223333")
    print("\nAfter editing John's phone:")
    print(john)

    found_phone = john.find_phone("5555555555") #Пошук конкретного телефону.
    print(f"\n{john.name}: {found_phone.value}")

    book.delete("Jane") #Видалення запису.
    print("\nAfter deleting Jane:")
    print(book)