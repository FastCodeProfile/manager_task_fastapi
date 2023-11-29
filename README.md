Для настройки проекта вам необходимо переименовать файл .env-dist в .env и ввести в него необходимые параметры.

Для установки всех зависимостей используем poetry/pip, команда(poetry): poetry install команда(pip) pip install -r requirements.txt


После чего вам необходимо провести миграции базы данных, для этого мы воспользуемся командой: alembic upgrade head


Теперь мы можем приступить к запуску проекта:

Для запуска FastAPI, воспользуемся командой: uvicorn app.__main__:app

Для запуска Celery Flower'a, воспользуемся командой: celery -A app.worker.celery flower

Для запуска Celery Worker'a, воспользуемся командой: celery -A app.worker.celery worker --loglevel=info -P eventlet
