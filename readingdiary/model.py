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









