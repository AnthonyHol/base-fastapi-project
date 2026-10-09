from core.config import settings
from core.enum import FileStorageEnum
from storages.fs import FileSystemStorage
from storages.s3 import S3Storage


def get_storage() -> type[FileSystemStorage | S3Storage]:
    if settings().FILE_STORAGE_TYPE == FileStorageEnum.FILESYSTEM:
        return FileSystemStorage
    else:
        return S3Storage
