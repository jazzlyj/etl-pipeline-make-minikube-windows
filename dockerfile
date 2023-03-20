FROM python:3.10.9-buster
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "etl.py"]