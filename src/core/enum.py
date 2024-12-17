"""File for describing enums."""

from enum import Enum


class FileStorageEnum(str, Enum):
    FILESYSTEM = "FILESYSTEM"
    S3 = "S3"
