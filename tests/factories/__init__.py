"""
Directory for db-models-based factories.

Try to put as many model attributes as possible into the factories to generate random values.
More about factories:
https://pytest-factoryboy.readthedocs.io/en/stable/
https://factoryboy.readthedocs.io/en/stable/introduction.html

Factory example:
from db.models import User
from tests.factories.base import BaseFactory
from tests.factories.fakers import UniqueStringFaker


class UserFactory(BaseFactory):
    username = UniqueStringFaker("first_name")

    class Meta:
        model = User
"""
