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

