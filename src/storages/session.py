import functools

from aioboto3.session import Session

from core.config import settings


@functools.lru_cache
def get_boto3_session() -> Session:
    return Session(
        aws_access_key_id=settings().S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings().S3_ACCESS_KEY_ID,
        region_name=settings().S3_ACCESS_KEY_ID,
    )
