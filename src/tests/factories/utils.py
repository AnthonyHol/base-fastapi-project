import random
import secrets
import uuid
from datetime import datetime, timedelta, date, time


def get_random_str() -> str:
    return str(uuid.uuid4())


def get_random_int(a: int = 1, b: int = 10) -> int:
    return random.randint(a, b)


def get_random_bytes() -> bytes:
    return secrets.token_bytes()


def get_random_datetime(datetime_start: datetime | None = None, datetime_end: datetime | None = None) -> datetime:
    if datetime_start is None:
        datetime_start = datetime(2015, 1, 1)
    if datetime_end is None:
        datetime_end = datetime.now()

    if datetime_start > datetime_end:
        raise ValueError("Начальная дата и время не могут быть позже конечной даты и времени")

    delta = (datetime_end - datetime_start).total_seconds()
    random_seconds = random.randint(0, int(delta))

    return datetime_start + timedelta(seconds=random_seconds)


def get_random_date(date_start: date | None = None, date_end: date | None = None) -> date:
    return get_random_datetime(
        datetime_start=datetime.combine(date_start, time()) if date_start else None,
        datetime_end=datetime.combine(date_end, time()) if date_end else None,
    ).date()
