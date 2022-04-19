from src.config import settings

bind = f'{settings.HOST}:{settings.PORT}'
workers = 4
threads = 4