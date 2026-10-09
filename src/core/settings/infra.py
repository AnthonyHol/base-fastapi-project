from pydantic import BaseModel


class InfraSettings(BaseModel):
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "base"

    REDIS_DSN: str = "redis://localhost:6379"

    S3_DSN: str = "http://localhost:9000"
    S3_ACCESS_KEY_ID: str = "base"
    S3_SECRET_ACCESS_KEY: str = "base"
    S3_REGION_NAME: str = "eu-central-1"
    S3_BUCKET_NAME: str = "base"

    @property
    def postgres_dsn(self) -> str:
        environment = getattr(self, "ENVIRONMENT", "local")
        database = self.POSTGRES_DB if environment != "test" else f"{self.POSTGRES_DB}_test"
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{database}"
        )
