class LibraryUser:
    def __init__(self, user_id, last_name, first_name, group, course):
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name
        self.group = group
        self.course = course
        self.borrowed_books = []
        self.returned_books = []

    def display_info(self):
        print("ID:", self.user_id)
        print("Прізвище:", self.last_name)
        print("Ім'я:", self.first_name)
        print("Група:", self.group)
        print("Курс:", self.course)
        print("Книги у боргу:", self.borrowed_books)
        print("Статистика книг:", self.returned_books)

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)
        print(f"Книга '{book_title}' успішно додана до списку боргу.")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            self.returned_books.append(book_title)
            print(f"Книга '{book_title}' успішно повернута.")
        else:
            print(f"Книга '{book_title}' відсутня у списку боргу.")


user_data = {
    "ID": 1,
    "прізвище": "Плещук",
    "Ім’я": "Володимир",
    "Група": "ІПЗс-2021-2",
    "Курс": 3,
    "Книги": [],
    "Статистика книг": []
}

user = LibraryUser(user_data["ID"], user_data["прізвище"], user_data["Ім’я"], user_data["Група"], user_data["Курс"])

user.display_info()

while True:
    print("\nМеню:")
    print("1. Вивести інформацію про читача")
    print("2. Взяти книгу у борг")
    print("3. Повернути книгу")
    print("0. Вийти з програми")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        user.display_info()
    elif choice == "2":
        book_to_borrow = input("Введіть назву книги, яку бажаєте взяти у борг: ")
        user.borrow_book(book_to_borrow)
    elif choice == "3":
        if user.borrowed_books:
            print("Книги у боргу:", user.borrowed_books)
            book_to_return = input("Введіть назву книги, яку бажаєте повернути: ")
            user.return_book(book_to_return)
        else:
            print("У вас немає книг у боргу.")
    elif choice == "0":
        print("Дякую за користування! До побачення!")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
