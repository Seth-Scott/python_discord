FROM python:3.8

ADD ./requirements.txt /
ADD ./main.py /

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]