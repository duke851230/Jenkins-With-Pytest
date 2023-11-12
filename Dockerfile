FROM python:3.11.1

COPY . /var/pytest

WORKDIR /var/pytest

RUN pip install -r /var/pytest/requirements.txt

CMD ["python", "test.py"]
