from django. core.management.base import BaseCommand

from django.utils import timezone
from django_seed import  Seed
from blog.models import Post



class Command(BaseCommand):
    help = 'Создает тестовые (фейковые) посты для блога'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type = int,
            default = 10,
            help = 'Сколько постов создать (по умолчанию создаю 10)'
        )

    def handle(self, *args, **options):
        number = options['number']

        seeder = Seed.seeder(locale = 'ru_RU')
        seeder.add_entity(Post, number, {
            'title': lambda x: seeder.faker.sentence(nb_words=4),
            'text': lambda x: seeder.faker.paragraph(nb_sentences=4),
            'created': lambda x: timezone.now(),
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'Постов созданно: {number}'))