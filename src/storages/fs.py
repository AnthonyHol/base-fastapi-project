import os

import aiofiles
from loguru import logger

from core.config import settings
from storages.base import BaseStorage


class FileSystemStorage(BaseStorage):
    _storage_dsn = str(settings().BASE_DIR)

    async def upload_file(self, key: str | None, data: bytes, content_type: str | None) -> bool:
        if key is None:
            return False

        file_path = self.get_path(key=key)

        if file_path is None:
            return False

        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            async with aiofiles.open(file_path, "wb") as file:
                await file.write(data)

            return True

        except Exception as e:
            logger.error(f"Unable to upload file {key}: {e}")
            return False

    async def delete_file(self, key: str | None) -> bool:
        if key is None:
            return False

        file_path = self.get_path(key=key)

        if file_path is None:
            return False

        try:
            os.remove(file_path)
            return True

        except FileNotFoundError:
            logger.error(f"File {key} not found.")
            return False

        except Exception as e:
            logger.error(f"Unable to delete file {key}: {e}")
            return False

    async def is_file_exists(self, key: str | None) -> bool:
        if key is None:
            return False

        file_path = self.get_path(key=key)

        if file_path is None:
            return False

        try:
            async with aiofiles.open(file_path, "rb"):
                pass

            return True

        except FileNotFoundError:
            logger.error(f"File {key} not found.")
            return False

        except Exception as e:
            logger.error(f"Unable to get head object {key}: {e}")
            return False

    async def generate_presigned_url(
        self,
        key: str | None,
        method: str = "get_object",
        expires_in: int = settings().PRESIGNED_FILE_URL_EXPIRATION_TIME,
    ) -> str | None:
        if key is None:
            return None

        return self.get_path(key=key)
