FROM python:3.9

ADD app.py .
ADD database.py .
ADD tests.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]