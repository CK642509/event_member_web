from pydantic import BaseConfig
class Settings(BaseConfig):
    """
    Configuration class for the application.
    """
    debug: bool = False
    port: int = 8080
    # host: str = '127.0.0.1'
    host: str = 'localhost'