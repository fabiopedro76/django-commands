from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imprime "Está Funcionando neste APP!"'

    def handle(self, *args, **options):
        self.stdout.write('Está Funcionando neste APP!')
