from django.core.management.base import BaseCommand
from webLib.models import Author, Book

class Command(BaseCommand):
    help = 'Checking DB / Проверяет Базу данных'

    def add_arguments(self, parser):
        parser.add_argument('book_ids', help='book_id', type=int, nargs='+')

    def handle(self, *args, **kwargs):
        book_ids = kwargs['book_ids']

        
        for book_id in book_ids:
            try:
                book_check = Book.objects.get(pk=book_id)
                self.stdout.write(self.style.SUCCESS('Книга с параметром == "%s" ис иес фоунд' % book_id))
            except Book.DoesNotExist:
                self.stdout.write(self.style.ERROR('Книга с параметром == "%s" ис ноут фоунд' % book_id))