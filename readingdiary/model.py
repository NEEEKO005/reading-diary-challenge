from datetime import datetime

class Note:

    def __init__(self, text: str,page: int,date: datetime):
        self.text:str = text
        self.page:int = page
        self.date:datetime = date

    def __str__(self) -> str :
        return f"{self.date} -page {self.page}:{self.text}"

class Book:

    Excelent:int=3
    Good:int=2
    Bad:int=1
    Unrated:int=0

    def __init__(self, isbn:str, title:str,author:str,page:int):
        self.isbn:str = isbn
        self.title:str = title
        self.author:str = author
        self.page:int = page
        self.rating:int = Book.Unrated
        self.notes:list[Note] = []

    def add_note(self,text:str,page:int,date:datetime )->bool:
        if page> self.page or page < 0:
            return False
        new_note = Note(text,page,date)
        self.notes.append(new_note)
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.Excelent, Book.Good, Book.Bad):
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self,page:int) -> list[Note]:
        return [note for note in self.notes if note.page == page]


    def page_with_most_notes(self)-> int:
        if not self.notes:
            return -1

        page_count = {}
        for note in self.notes:
            page_count[note.page] = page_count.get(note.page, 0) + 1

        return max(page_count, key=page_count.get)

    def __str__(self) -> str:
        rating_str = {
            Book.Excelent: "excellent",
            Book.Good: "good",
            Book.Bad: "bad",
            Book.Unrated: "unrated"
        }.get(self.rating, "unrated")

        return (f"ISBN: {self.isbn}\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Pages: {self.page}\n"
                f"Rating: {rating_str}")









