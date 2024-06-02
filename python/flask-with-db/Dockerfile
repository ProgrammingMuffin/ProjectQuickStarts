FROM python:3.12.3-bookworm

COPY ./hello_world ./hello_world
COPY ./app.py ./app.py
COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN pwd
RUN ls

CMD ["python", "./app.py"]