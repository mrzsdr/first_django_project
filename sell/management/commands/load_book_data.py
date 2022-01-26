from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from sell.models import Book

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet model"

    def handle(self, *args, **options):
        if Book.objects.exists():
            print('Book data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading Book data for Book available for selling")
        for row in DictReader(open('./bookdata.csv')):
            book = Book()
            book.name = row['Name']
            book.author = row['Author']
            book.year = row['Year']
            book.genre = row['Genre'] 
            book.save()
            
