import csv
from django.core.management.base import BaseCommand
from katalog.models import Book

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csvfile = kwargs['csvfile']
        max_books = 100

        with open(csvfile, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                # Sesuaikan dengan nama kolom CSV dan model Anda
                book = Book.objects.create(
                    title=row['title'],
                    authors=row['authors'],
                    average_rating=row['average_rating'],
                    isbn=row['isbn'],
                    isbn13=row['isbn13'],
                    language_code=row['language_code'],
                    num_pages=row['  num_pages'],
                    ratings_count=row['ratings_count'],
                    text_reviews_count=row['text_reviews_count'],
                    publication_date=row['publication_date'],
                    publisher=row['publisher'],
                    # Sesuaikan atribut lainnya sesuai kebutuhan
                )
                count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully imported book: {book.title}'))

                if count >= max_books:
                    self.stdout.write(self.style.SUCCESS(f'Import limit reached. Stopping import.'))
                    break
