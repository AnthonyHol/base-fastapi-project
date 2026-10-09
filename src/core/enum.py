"""File for describing enums."""

from enum import StrEnum


class FileStorageEnum(StrEnum):
    FILESYSTEM = 'FILESYSTEM'
    S3 = 'S3'
