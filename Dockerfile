FROM python:3 as base-py
WORKDIR /app

COPY requirments.txt .

RUN pip install -r requirments.txt


FROM base-py as http-server

WORKDIR /app/src/

COPY src/. .

WORKDIR /app

COPY src/server/flask_sorting.py .

COPY gunicorn.conf.py .


FROM base-py as unit-tests

WORKDIR /app/src/logic

COPY src/logic .

WORKDIR /app

COPY tests/unit/tests.py .

CMD ["python","-m",  "pytest", "tests.py"]


FROM base-py as integr-tests

WORKDIR /app/src/

COPY src/config.py .

WORKDIR /app

COPY tests/integrational/tests.py .

CMD ["python","-m",  "pytest", "tests.py"]
