class Url:
    def __init__(self, base_url: str, params: dict):
        self.base_url = base_url
        self.url = self.add_query_params(params)

    def add_query_params(self, params: list) -> str:
        if not params:
            return self.base_url

        query_string = "&".join(f"{key}={value}" for key, value in params.items())
        return f"{self.base_url}{query_string}"

    def get(self) -> str:
        return self.url

    def __str__(self):
        return self.url
