import os

from pydantic import BaseSettings


class Base(BaseSettings):
    HOST: str = os.getenv('HOST', '127.0.0.1')
    PORT: int = os.getenv('PORT', 8080)
    DB_HOST: str = os.getenv('DB_HOST', '127.0.0.1')
    DB_PORT: int = os.getenv('DB_PORT', 27017)
    DB_NAME: str = os.getenv('DB_NAME', 'sorting_db')


settings = Base()
