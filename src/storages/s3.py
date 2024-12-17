import io
import os

import botocore.exceptions
from aioboto3.session import Session
from fastapi import Depends
from loguru import logger

from core.config import settings
from storages.session import get_boto3_session
from storages.utils import get_updated_path_depending_on_os


class S3Storage:
    def __init__(self, boto3_session: Session = Depends(get_boto3_session)) -> None:
        self._boto3_session = boto3_session

        self._s3_url = settings().S3_DSN
        self._s3_bucket_name = settings().S3_BUCKET_NAME

        self._storage_dsn = os.path.join(
            self._s3_url,
            self._s3_bucket_name,
        )

    def get_path(self, key: str | None) -> str | None:
        """
        Return the full path to the file.

        :param key: the key of the file in the repository (example: "media/file.txt").
        :return: full path to the file or None (example: "http://localhost:9000/media/file.txt").
        """

        if key is None:
            return None

        return get_updated_path_depending_on_os(os.path.join(self._storage_dsn, key))

    async def upload_file(self, key: str | None, data: bytes, content_type: str | None) -> str | None:
        """
        Load the file into the repository.

        :param key: the key of the file in the repository (example: "files/file.txt").
        :param data: the file data in bytes.
        :param content_type: the content type of the file data.
        :return: the value indicating the success of the operation.
        """

        if key is None:
            return None

        content = io.BytesIO(data)

        try:
            async with self._boto3_session.client("s3", endpoint_url=self._s3_url) as s3_client:
                await s3_client.upload_fileobj(
                    Fileobj=content,
                    Bucket=self._s3_bucket_name,
                    Key=key,
                    ExtraArgs={"ContentType": content_type},
                )

            return key

        except (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError) as e:
            logger.error(f"Unable to upload file '{key}': {e}")
            return None

    async def delete_file(self, key: str | None) -> bool:
        """
        Delete the file from storage.

        :param key: the key of the file in the repository (example: "files/file.txt").
        :return: the value indicating the success of the operation.
        """

        if key is None:
            return False

        try:
            async with self._boto3_session.client("s3", endpoint_url=self._s3_url) as s3_client:
                await s3_client.delete_object(Bucket=self._s3_bucket_name, Key=key)

            return True

        except (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError) as e:
            logger.error(f"Unable to delete file {key}: {e}")
            return False

    async def is_file_exists(self, key: str | None) -> bool:
        """
        Return an indication that the file exists.

        :param key: the key of the file in the repository.
        :return: sign of file existence.
        """

        if key is None:
            return False

        try:
            async with self._boto3_session.client("s3", endpoint_url=self._s3_url) as s3_client:
                await s3_client.head_object(Bucket=self._s3_bucket_name, Key=key)

            return True

        except (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError) as e:
            logger.error(f"Unable to get head object '{key}': {e}")
            return False

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

        if key is None:
            return None

        try:
            async with self._boto3_session.client("s3", endpoint_url=self._s3_url) as s3_client:
                return await s3_client.generate_presigned_url(
                    method, Params={"Bucket": self._s3_bucket_name, "Key": key}, ExpiresIn=expires_in
                )

        except (botocore.exceptions.BotoCoreError, botocore.exceptions.ClientError) as e:
            logger.error(f"Unable to get head object '{key}': {e}")
            return None
