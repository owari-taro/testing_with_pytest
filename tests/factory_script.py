from dataclasses import dataclass
from faker import Faker

from factory import Factory,SubFactory

fake = Faker('ja_jp')
from datetime import datetime


@dataclass 
class Author:
    name:str
    address:str

@dataclass
class Book:
    name:str
    date:datetime
    price:str
    author:Author

class AuthorFactory(Factory):
    class Meta:
        model=Author
    name=fake.name()
    address=fake.address()


class BookFactory(Factory):
    class Meta:
        model=Book
    name=fake.name()
    date=str(fake.date_between())
    price=fake.pricetag()
    author=SubFactory(AuthorFactory)

AuthorFactory()
