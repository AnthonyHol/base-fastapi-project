from typing import Type

from core.config import settings
from core.enums import FileStorageEnum
from storages.fs import FileSystemStorage
from storages.s3 import S3Storage


def get_storage() -> Type[FileSystemStorage | S3Storage]:
    if settings().FILE_STORAGE_TYPE == FileStorageEnum.FILESYSTEM:
        return FileSystemStorage
    else:
        return S3Storage
