from pydantic import BaseModel

from core.enum import FileStorageEnum


class StorageSettings(BaseModel):
    FILE_STORAGE_TYPE: FileStorageEnum = FileStorageEnum.S3
    STORAGE_FILE_PATH: str = 'base/dir/'
    PRESIGNED_FILE_URL_EXPIRATION_TIME: int = 3600
