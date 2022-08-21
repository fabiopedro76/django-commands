from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imprime o "Olá Mundo!"'

    def handle(self, *args, **options):
        self.stdout.write('Olá Mundo!')
