from pydantic_settings import BaseSettings, SettingsConfigDict


class AtacApiSettings(BaseSettings):
    atac_base_url: str
    atac_proxy_path: str
    atac_timings_endpoint: str

    @property
    def atac_url(self) -> str:
        return f"{self.atac_base_url}{self.atac_proxy_path}"

    @property
    def atac_timings_url(self) -> str:
        return f"{self.atac_url}{self.atac_timings_endpoint}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="ATAC_",
    )


atac = AtacApiSettings()
