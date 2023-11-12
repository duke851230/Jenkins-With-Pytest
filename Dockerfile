FROM python:3.11.1

COPY . /var/pytest

WORKDIR /var/pytest

RUN pip install -r /var/pytest/requirements.txt

# 使用「exit $PIPESTATUS」讓 Docker 以當前的 exit code 退出容器，這樣 Jenkins 才能抓到正確的 exit code
CMD /bin/sh -c "python test.py; exit $PIPESTATUS"
