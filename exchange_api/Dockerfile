FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /feedback/requirements.txt
RUN pip install --no-cache-dir -r /feedback/requirements.txt

COPY . /test

WORKDIR /test

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7050"]