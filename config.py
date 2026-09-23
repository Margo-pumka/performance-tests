from pydantic_settings import BaseSettings, SettingsConfigDict

from tools.config.grpc import GRPCClientConfig
from tools.config.http import HTTPClientConfig
from tools.config.locust import LocustUserConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter='.',
        extra="allow"
    )
    locust_user: LocustUserConfig
    gateway_http_client: HTTPClientConfig
    gateway_grpc_client: GRPCClientConfig


settings = Settings()
