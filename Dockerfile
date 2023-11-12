FROM python:3.11.1

COPY . /var/pytest

RUN pip install -r /var/pytest/requirements.txt

WORKDIR /var/pytest

CMD ["python", "test.py"]
