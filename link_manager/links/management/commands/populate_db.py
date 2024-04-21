from django.core.management.base import BaseCommand
from faker import Faker
from links.models import Link, Collection
from links.models import CustomUser
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        faker = Faker()

        users = []
        for _ in range(25):
            user = CustomUser.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                password="password"
            )
            users.append(user)

        for user in users:
            for _ in range(10):
                collection = Collection.objects.create(
                    name=faker.word(),
                    description=faker.sentence(),
                    user=user
                )

                for _ in range(5):
                    link = Link.objects.create(
                        title=faker.sentence(),
                        description=faker.paragraph(),
                        url=faker.url(),
                        image=faker.image_url(),
                        link_type=random.choice(["website", "book", "article", "music", "video"]),
                        user=user
                    )
                    link.collections.add(collection)

        self.stdout.write(self.style.SUCCESS("The database is filled with random data."))
