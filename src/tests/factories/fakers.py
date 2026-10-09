import typing

from factory.builder import BuildStep
from factory.faker import Faker


class UniqueFaker(Faker):
    def evaluate(self, instance: typing.Any, step: BuildStep, extra: typing.Any) -> typing.Any:
        extra = {"locale": "en_US"}
        value = super().evaluate(instance, step, extra)  # type: ignore[no-untyped-call]
        return value


class UniqueStringFaker(UniqueFaker):
    def evaluate(self, instance: typing.Any, step: BuildStep, extra: typing.Any) -> str:
        value = super().evaluate(instance, step, extra)
        return f"{step.sequence}_{value}"
