class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.__class__.all_books.append(self)

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.__class__.all_authors.append(self)

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        total = sum(contract.royalties for contract in self.contracts_list)
        return total

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object")
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        if not isinstance(date, str):
            raise Exception("Date should be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties should be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

# Test the implementation
if __name__ == "__main__":
    # Creating books
    book1 = Book("Python Programming")
    book2 = Book("Data Science Essentials")

    # Creating authors
    author1 = Author("John Doe")

    # Signing contracts
    contract1 = author1.sign_contract(book1, "2024-05-30", 10)
    contract2 = author1.sign_contract(book2, "2024-05-30", 15)

    # Accessing contracts and books for an author
    print("Contracts for Author 1:", [contract.book.title for contract in author1.contracts()])
    print("Books for Author 1:", [book.title for book in author1.books()])

    # Total royalties for an author
    print("Total royalties for Author 1:", author1.total_royalties())

    # Contracts by date
    print("Contracts on 2024-05-30:", [contract.book.title for contract in Contract.contracts_by_date("2024-05-30")])
