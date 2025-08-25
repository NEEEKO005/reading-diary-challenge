from datetime import datetime

class Note:

    def __init__(self, text: str,page: int,date: datetime):
        self.text:str = text
        self.page:int = page
        self.date:datetime = date
