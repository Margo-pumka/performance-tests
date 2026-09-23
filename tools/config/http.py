from pydantic import HttpUrl, BaseModel


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float = 100.0

    @property
    def client_url(self) -> str:
        return str(self.url)
