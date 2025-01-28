import os

from core.config import settings
from storages.utils import get_updated_path_depending_on_os


class BaseStorage:
    """
    Base class for storage

    _storage_dsn - path to the storage.
    """

    _storage_dsn: str

    def get_path(self, key: str | None) -> str | None:
        """
        Return the full path to the file.

        :param key: the key of the file in the repository (example: "media/file.txt").
        :return: full path to the file or None (example: "http://localhost:9000/media/file.txt").
        """
        if key is None:
            return None

        return get_updated_path_depending_on_os(
            os.path.join(os.path.join(self._storage_dsn, settings().STORAGE_FILE_PATH), key)
        )

    async def upload_file(self, key: str | None, data: bytes, content_type: str | None) -> bool:
        """
        Load the file into the repository.

        :param key: the key of the file in the repository (example: "files/file.txt").
        :param data: the file data in bytes.
        :param content_type: the content type of the file data.
        :return: the value indicating the success of the operation.
        """

        raise NotImplementedError

    async def delete_file(self, key: str | None) -> bool:
        """
        Delete the file from storage.

        :param key: the key of the file in the repository (example: "files/file.txt").
        :return: the value indicating the success of the operation.
        """
        raise NotImplementedError

    async def is_file_exists(self, key: str | None) -> bool:
        """
        Return an indication that the file exists.

        :param key: the key of the file in the repository.
        :return: sign of file existence.
        """
        raise NotImplementedError

    async def generate_presigned_url(
        self,
        key: str | None,
        method: str = "get_object",
        expires_in: int = settings().PRESIGNED_FILE_URL_EXPIRATION_TIME,
    ) -> str | None:
        """
        Generate a signed url to the file.

        :param key: the key of the file in the repository.
        :param method: the method for which the url is generated.
        :param expires_in: the value of the link lifetime in seconds.
        :return: the signed url to the file.
        """
        raise NotImplementedError
