import typing

from faker import Faker
from faker.generator import random

from apps.contacts import models


def create_a_phone():

    suffix = random.randint(999999, 10000000)

    return f"+38067{suffix}"


def contacts_generate(amount: int = 10) -> typing.Iterator[models.Contacts]:
    fake = Faker()

    for _ in range(amount):
        yield models.Contacts(name=fake.first_name() + " " + fake.last_name(), phone=create_a_phone())
