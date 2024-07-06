class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.issued_books = []

    def issue_book(self, book):
        self.issued_books.append(book)

    def return_book(self, book):
        self.issued_books.remove(book)

class Librarian:
    def __init__(self, name):
        self.name = name

    def add_book(self, library, book):
        library.books.append(book)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def issue_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if member and book:
            member.issue_book(book)
            self.books.remove(book)
            return f"Book '{book_title}' issued to member '{member.name}'."
        else:
            return "Book or member not found."

    def return_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            book = next((b for b in member.issued_books if b.title == book_title), None)
            if book:
                member.return_book(book)
                self.books.append(book)
                return f"Book '{book_title}' returned by member '{member.name}'."
        return "Book or member not found."

def main():
    library = Library()
    librarian = Librarian("Sarah")

    while True:
        print("\nLibrary Management System")
        print("1. Add Member")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter member name: ")
            member_id = int(input("Enter member ID: "))
            member = Member(name, member_id)
            library.add_member(member)
            print(f"Member '{name}' added with ID '{member_id}'.")

        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year_published = int(input("Enter year published: "))
            book = Book(title, author, year_published)
            librarian.add_book(library, book)
            print(f"Book '{title}' by '{author}' added.")

        elif choice == '3':
            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title: ")
            result = library.issue_book(member_id, book_title)
            print(result)

        elif choice == '4':
            member_id = int(input("Enter member ID: "))
            book_title = input("Enter book title: ")
            result = library.return_book(member_id, book_title)
            print(result)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
