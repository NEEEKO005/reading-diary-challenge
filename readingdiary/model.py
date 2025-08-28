from datetime import datetime

class Note:

    def __init__(self, text: str,page: int,date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str :
        return f"{self.date} -page {self.page}:{self.text}"

class Book:

    EXCELENT: int= 3
    GOOD: int= 2
    BAD: int= 1
    UNRATED: int= -1

    def __init__(self, isbn:str, title:str,author:str,page:int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.page: int = page
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self,text:str,page:int,date:datetime ) -> bool:
        if page> self.page:
            return False

        note: Note = Note(text,page,date)
        self.notes.append(note)
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in [Book.EXCELENT, Book.GOOD, Book.BAD]:
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self,page:int) -> list[Note]:
        return [note for note in self.notes if note.page == page]


    def page_with_most_notes(self) -> int:
        notes_counter:dict[int, int]= {}
        for note in self.notes:
            if note.page not in notes_counter:
                notes_counter[note.page]=1
            else:
                notes_counter[note.page] +=1

        max_page, max_counter = -1 , 0
        for page, count in notes_counter.items():
            if count > max_counter:
                max_page,max_counter=page,count

        return max_page



    def __str__(self) -> str:
        rating_str = {
            Book.EXCELENT: "excellent",
            Book.GOOD: "good",
            Book.BAD: "bad",
            Book.UNRATED: "unrated"
        }.get(self.rating, "unrated")

        return f"ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nPages: {self.page}\nRating: {rating_str[self.rating]}"

class ReadingDiary:

    def __init__(self):
        self.books: dict[str, Book]= {}

    def add_book(self, isbn: str,title: str,author: str,pages: int) -> bool :
        if isbn in self.books:
            return False
        self.books[isbn]=Book(isbn,title,author,pages)
        return True

    def search_by_isbn(self,isbn: str) -> Book :
        return self.books.get(isbn, None)

    def add_note_to_book(self, isbn: str,text: str,page: int, date: datetime):
        book: Book = self.books.get(isbn)
        if not book:
            return False

        return book.add_note(text,page,date)



    def rate_book(self,isbn: str,rating: int) -> bool:
        book: Book = self.books.get(isbn)
        if not book:
            return False

        return book.set_rating(rating)

    def book_with_most_note(self) -> Book | None:
        target_book, most_notes = None, 0

        for book in self.books.values():
            if len(book.notes) > most_notes:
                target_book,most_notes= book, len(book.notes)

        return target_book











